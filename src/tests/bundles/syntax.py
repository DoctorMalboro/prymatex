# -*- coding: utf-8 -*-

import re
import ipdb
import plistlib
from debug_processor import DebugProcessor

class SyntaxProxy(object):
    def __init__(self, hash, syntax):
        self.syntax = syntax
        self.proxy = hash['include']
    
    def __getattr__(self, name):
        if self.proxy:
            proxy_value = self.__proxy()
            if proxy_value:
                return getattr(proxy_value, name)
            #TODO: else raise exception
    
    def __proxy(self):
        if re.compile('^#').match(self.proxy):
            return self.syntax.repository[self.proxy[1:]]
        elif "$self":
            return self.syntax
        elif "$base":
            return self.syntax
        else:
            return self.syntax.syntaxes[self.proxy]


def parse_file(filename, name_space = 'default'):
    data = plistlib.readPlist(filename)
    return SyntaxNode(data, None, name_space)

class SyntaxNode(object):
    OPTIONS = re.UNICODE
    syntaxes = {}
    
    def __init__(self, hash, syntax = None, name_space = 'default'):
        for k in ['syntax', 'firstLineMatch', 'foldingStartMarker', 'foldingStopMarker', 'match', 
                  'begin', 'content', 'fileTypes', 'name', 'contentName', 'end', 'scopeName', 'keyEquivalent',
                  'captures', 'beginCaptures', 'endCaptures', 'repository', 'patterns']:
            setattr(self, k, None)
        self.name_space = name_space
        self.__class__.syntaxes.setdefault(self.name_space, {})
        if 'scopeName' in hash:
            self.__class__.syntaxes[self.name_space][hash["scopeName"]] = self 
        self.syntax = syntax or self
        for key, value in hash.iteritems():
            if key in ["firstLineMatch", "foldingStartMarker", "foldingStopMarker", "match", "begin"]:
                try:
		    # Estos replace hay que sacarlos si usamos el motor de expreciones de la dll
                    value = value.replace('?i:', '(?i)')
                    value = value.replace('?x:', '(?x)')
                    value = value.replace('?<=', '(?<=)')
                    setattr(self, key, re.compile( value ))
                except:
                  print "Parsing error in %s: %s" % (key, value)
            elif key in ["content", "fileTypes", "name", "contentName", "end", "scopeName", "keyEquivalent"]:
                setattr(self, key, value )
            elif key in ["captures", "beginCaptures", "endCaptures"]:
                keys = map(lambda v: int(v), value.keys())
                value = map(lambda v: value["%s" % (v)], keys)
                setattr(self, key, value.sort() )
            elif key == "repository":
                self.parse_repository(value)
            elif key in ["patterns"]:
                self.create_children(value)
            else:
                print u"Ignoring: %s: %s" % (key, value)
    
    def parse(self, string, processor = None ):
        if processor:
            processor.start_parsing(self.scopeName)
        stack = [[self, None]]
        for line in string.splitlines():
           self.parse_line(stack, line, processor)
        if processor:
            processor.end_parsing(self.scopeName)
        return processor
    
    def parse_repository(self, repository):
         self.repository = {}
         for key, value in repository.iteritems():
            if 'include' in value:
               self.repository[key] = SyntaxProxy( value, self.syntax )
            else:
               self.repository[key] = SyntaxNode( value, self.syntax, self.name_space )

    def create_children(self, patterns):
         self.patterns = []
         for p in patterns:
            if 'include' in p:
                self.patterns.append(SyntaxProxy( p, self.syntax ))
            else:
                self.patterns.append(SyntaxNode( p, self.syntax, self.name_space ))
    
    def parse_captures(self, name, pattern, match, processor):
        captures = pattern.match_captures( name, match )
        #reject en ruby para python niego
        captures = filter(lambda group, range, name: range[0] and range[0] != range[-1], captures)
        starts = []
        ends = []
        for group, range, name in captures:
            starts.append([range.first, group, name])
            ends.append([range.last, -group, name])
        starts = starts[::-1]
        ends = ends[::-1]
         
        while starts or ends:
            if starts:
                pos, key, name = ends.pop()
                processor.close_tag(name, pos)
            elif ends:
                pos, key, name = starts.pop
                processor.open_tag(name, pos)
            elif abs(ends[-1][1]) < starts[-1][1]:
                pos, key, name = ends.pop()
                processor.close_tag(name, pos)
            else:
                pos, key, name = starts.pop()
                processor.open_tag(name, pos)
    
    def match_captures(self, name, match):
        matches = []
        captures = getattr(self, name)
        if captures:
            for key, value in captures:
                if not re.compile('^\d*$').match(key):
                    if int(key) < len(match):
                        matches.append([int(key), match.offset( int(key) ), value["name"]])
                else:
                    if match.to_index( key.to_sym ):
                        matches.append([match.to_index( key.to_sym ), match.offset( key.to_sym), value["name"]])
        return matches
        
    def match_first(self, string, position):
        if self.match:
            match = self.match.search( string, position )
            if match:
                return (self, match) 
        elif self.begin:
            match = self.begin.search( string, position )
            if match:
                return (self, match) 
        elif self.end:
           pass
        else:
           return self.match_first_son( string, position )
        return (None, None)
    
    def match_end(self, string, match, position):
        regstring = self.end[:]
        def g_match(mobj):
            ipdb.set_trace()
            index = int(mobj.group(0))
            return match.group(index)
        def d_match(mobj):
            ipdb.set_trace()
            index = mobj.group(0)
            return match.groupdict(index)
        regstring = re.sub(re.compile('\\\\([1-9])'), g_match, regstring)
        regstring = re.sub(re.compile('\\\\k<(.*?)>'), d_match, regstring)
        return re.compile( regstring, re.UNICODE).search( string, position )
    
    def match_first_son(self, string, position):
        match = (None, None)
        if self.patterns:
            for p in self.patterns:
                tmatch = p.match_first(string, position)
                if tmatch[1]:
                    if not match[1] or match[1].start() > tmatch[1].start():
                        match = tmatch
        return match
      
    def parse_line(self, stack, line, processor):
        if processor:
            processor.new_line(line)
        top, match = stack[-1]
        position = 0
            
        while True:
            if top.patterns:
                pattern, pattern_match = top.match_first_son(line, position)
            else:
                pattern, pattern_match = None, None
            end_match = None
            if top.end:
                end_match = top.match_end( line, match, position )
            
            if end_match and ( not pattern_match or pattern_match.start() >= end_match.start() ):
               pattern_match = end_match
               start_pos = pattern_match.start()
               end_pos = pattern_match.end()
               if top.contentName and processor:
                   processor.close_tag(top.contentName, start_pos)
               if processor:
                   self.parse_captures("captures", top, pattern_match, processor)
               if processor:
                   self.parse_captures("endCaptures", top, pattern_match, processor)
               if top.name and processor:
                   processor.close_tag( top.name, end_pos)
               stack.pop()
               top, match = stack[-1]
            else:
               if not pattern:
                   break 
               start_pos = pattern_match.start()
               end_pos = pattern_match.end()
               if pattern.begin:
                   if pattern.name and processor:
                       processor.open_tag(pattern.name, start_pos)
                   if processor:    
                       self.parse_captures("captures", pattern, pattern_match, processor)
                   if processor:
                       self.parse_captures("beginCaptures", pattern, pattern_match, processor)
                   if pattern.contentName and processor:
                       processor.open_tag(pattern.contentName, end_pos)
                   top = pattern
                   match = pattern_match
                   stack.append([top, match])
               elif pattern.match:
                   if pattern.name and processor:
                       processor.open_tag(pattern.name, start_pos)
                   if processor:
                       self.parse_captures("captures", pattern, pattern_match, processor)
                   if pattern.name and processor:
                       processor.close_tag(pattern.name, end_pos)
            position = end_pos
        return position

if __name__ == '__main__':
    python = parse_file('./Python.tmLanguage', 'python')
    json = parse_file('./JSON.tmLanguage', 'json')
    p = DebugProcessor()
    print python.parse(open('./debug_processor.py', 'r').read(), p)
    print json.parse('{"hola": "mundo", "estas": [1,2,3,"re","loco"]}', p)
    ipdb.set_trace()