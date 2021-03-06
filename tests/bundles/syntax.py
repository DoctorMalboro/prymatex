#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Syntax's module
        content, name, scope, keyEquivalent, tabTrigger
'''

import re
import ipdb
import plistlib

TM_SYNTAXES = {}

######################### SyntaxProcessor #################################

class TMSyntaxProcessor(object):
    '''
        Syntax Processor, clase base para los procesadores de sintaxis
    '''
    def __init__(self):
        pass

    def open_tag(self, name, position):
        pass

    def close_tag(self, name, position):
        pass

    def new_line(self, line):
        pass

    def start_parsing(self, name, position):
        pass

    def end_parsing(self, name, position):
        pass

class TMDebugSyntaxProcessor(TMSyntaxProcessor):
    def __init__(self):
        self.line_number = 0
        self.printable_line = ''

    def pprint(self, line, string, position = 0):
        line = line[:position] + string + line[position:]
        return line

    def open_tag(self, name, position):
        print self.pprint( '', '{ %s' % name, position + len(self.line_marks))

    def close_tag(self, name, position):
        print self.pprint( '', '} %s' % name, position + len(self.line_marks))

    def new_line(self, line):
        self.line_number += 1
        self.line_marks = '[%04s] ' % self.line_number
        print '%s%s' % (self.line_marks, line)

    def start_parsing(self, name, position):
        print '{%s' % name

    def end_parsing(self, name, position):
        print '}%s' % name

################################## ScoreManager ###################################

class TMScoreManager(object):
    POINT_DEPTH    = 4
    NESTING_DEPTH  = 40
    START_VALUE    = 2 ** ( POINT_DEPTH * NESTING_DEPTH )
    BASE           = 2 ** POINT_DEPTH
      
    def __init__(self):
        self.scores = {}
    
    def score(self, search_scope, reference_scope):
        maxi = 0
        for scope in search_scope.split( ',' ):
            arrays = re.compile("\B-").split(scope)
            if len(arrays) == 1:
                maxi = max([maxi, self.score_term( arrays[0], reference_scope )])
            elif len(arrays) > 1:
                excluded = False
                for a in arrays[1:]:
                    if self.score_term( a, reference_scope ) > 0:
                        excluded = True
                        break
                if not excluded:
                    maxi = max([maxi, self.score_term( arrays[0], reference_scope )])
            elif len(arrays) < 1:
                raise Exception("Error in scope string: '%s' %s is not a valid number of operands" % (search_scope, len(arrays)))
        return maxi
    
    def score_term(self, search_scope, reference_scope):
        if not (self.scores.has_key(reference_scope) and self.scores[reference_scope].has_key(search_scope)):
            self.scores.setdefault(reference_scope, {})
            self.scores[reference_scope][search_scope] = self.score_array( search_scope.split(' '), reference_scope.split( ' ' ) )
        return self.scores[reference_scope][search_scope]
      
    def score_array(self, search_array, reference_array):
        pending = search_array
        current = reference_array[-1]
        reg = re.compile( "^%s" % re.escape( pending[-1] ))
        multiplier = self.START_VALUE
        result = 0
        while len(pending) > 0 and current:
            match = reg.match(current)
            if match:
                point_score = (2 ** self.POINT_DEPTH) - current.count( '.' ) + match.group().count( '.' )
                result += point_score * multiplier
                pending.pop()
                if len(pending) > 0:
                    reg = re.compile( "^%s" % re.escape( pending[-1] ) )
            multiplier = multiplier / self.BASE
            reference_array.pop()
            current = reference_array and reference_array[-1] or None
        if len(pending) > 0:
            result = 0
        return result

############################## Syntax ######################################

class TMSyntaxProxy(object):
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
            if hasattr(self.syntax, 'repository') and self.syntax.repository.has_key(self.proxy[1:]):  
                return self.syntax.repository[self.proxy[1:]]
        elif self.proxy == '$self':
            return self.syntax
        elif self.proxy == '$base':
            return self.syntax
        else:
            return self.syntax.syntaxes[self.proxy]

class TMSyntaxNode(object):
    OPTIONS = re.UNICODE
    
    def __init__(self, hash, syntax = None, name_space = 'default'):
        for k in ['syntax', 'firstLineMatch', 'foldingStartMarker', 'foldingStopMarker', 'match', 
                  'begin', 'content', 'fileTypes', 'name', 'contentName', 'end', 'scopeName', 'keyEquivalent',
                  'captures', 'beginCaptures', 'endCaptures', 'repository', 'patterns']:
            setattr(self, k, None)
        self.name_space = name_space
        TM_SYNTAXES.setdefault(self.name_space, {})
        #Definicion de un scope
        if 'scopeName' in hash:
            TM_SYNTAXES[self.name_space][hash['scopeName']] = self 
        self.syntax = syntax or self
        for key, value in hash.iteritems():
            if key in ['firstLineMatch', 'foldingStartMarker', 'foldingStopMarker', 'match', 'begin']:
                try:
                    # TODO: Estos replace hay que sacarlos si usamos el motor de expreciones de la dll
                    value = value.replace('?i:', '(?i)')
                    value = value.replace('?x:', '(?x)')
                    value = value.replace('?<=', '(?<=)')
                    setattr(self, key, re.compile( value ))
                except:
                    pass
                #print 'Parsing error in %s: %s' % (key, value)
            elif key in ['content', 'fileTypes', 'name', 'contentName', 'end', 'scopeName', 'keyEquivalent']:
                setattr(self, key, value )
            elif key in ['captures', 'beginCaptures', 'endCaptures']:
                keys = map(lambda v: int(v), value.keys())
                value = map(lambda v: value['%s' % (v)], keys)
                setattr(self, key, value.sort() )
            elif key == 'repository':
                self.parse_repository(value)
            elif key in ['patterns']:
                self.create_children(value)
            else:
                pass
                #print u'Ignoring: %s: %s' % (key, value)
                
    @property
    def syntaxes(self):
        return TM_SYNTAXES[self.name_space]
    
    def parse(self, string, processor = None, _stack = None):
        position = 0
        if processor:
            processor.start_parsing(self.scopeName, position)
        stack = _stack or [[self, None]]
        for line in string.splitlines():
            if processor:
                processor.new_line(line)
            position += self.parse_line(stack, line, processor)
        if processor:
            processor.end_parsing(self.scopeName, position)
        return stack
    
    def parse_repository(self, repository):
        self.repository = {}
        for key, value in repository.iteritems():
            if 'include' in value:
                self.repository[key] = TMSyntaxProxy( value, self.syntax )
            else:
                self.repository[key] = TMSyntaxNode( value, self.syntax, self.name_space )

    def create_children(self, patterns):
        self.patterns = []
        for p in patterns:
            if 'include' in p:
                self.patterns.append(TMSyntaxProxy( p, self.syntax ))
            else:
                self.patterns.append(TMSyntaxNode( p, self.syntax, self.name_space ))
    
    def parse_captures(self, name, pattern, match, processor):
        captures = pattern.match_captures( name, match )
        
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
                pos, _, name = ends.pop()
                processor.close_tag(name, pos)
            elif ends:
                pos, _, name = starts.pop
                processor.open_tag(name, pos)
            elif abs(ends[-1][1]) < starts[-1][1]:
                pos, _, name = ends.pop()
                processor.close_tag(name, pos)
            else:
                pos, _, name = starts.pop()
                processor.open_tag(name, pos)
    
    def match_captures(self, name, match):
        matches = []
        captures = getattr(self, name)
        if captures:
            for key, value in captures:
                if not re.compile('^\d*$').match(key):
                    if int(key) < len(match):
                        matches.append([int(key), match.offset( int(key) ), value['name']])
                else:
                    if match.to_index( key.to_sym ):
                        matches.append([match.to_index( key.to_sym ), match.offset( key.to_sym), value['name']])
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
            index = mobj.group(0)
            return match.group(index)
        def d_match(mobj):
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
                    self.parse_captures('captures', top, pattern_match, processor)
                if processor:
                    self.parse_captures('endCaptures', top, pattern_match, processor)
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
                        self.parse_captures('captures', pattern, pattern_match, processor)
                    if processor:
                        self.parse_captures('beginCaptures', pattern, pattern_match, processor)
                    if pattern.contentName and processor:
                        processor.open_tag(pattern.contentName, end_pos)
                    top = pattern
                    match = pattern_match
                    stack.append([top, match])
                elif pattern.match:
                    if pattern.name and processor:
                        processor.open_tag(pattern.name, start_pos)
                    if processor:
                        self.parse_captures('captures', pattern, pattern_match, processor)
                    if pattern.name and processor:
                        processor.close_tag(pattern.name, end_pos)
            position = end_pos
        return position

def parse_file(filename, name_space = 'default'):
    data = plistlib.readPlist(filename)
    return TMSyntaxNode(data, None, name_space)

def test_score():
    sp = TMScoreManager()
    reference_scope = 'text.html.basic source.php.embedded.html string.quoted.double.php'
   
    ipdb.set_trace()
    print 0 != sp.score( 'source.php string', reference_scope )
    ipdb.set_trace()
    print 0 != sp.score( 'text.html source.php', reference_scope )
    ipdb.set_trace()
    print 0 == sp.score( 'string source.php', reference_scope )
    ipdb.set_trace() 
    print 0 == sp.score( 'source.php text.html', reference_scope ) 
    
    ipdb.set_trace()
    print 0 == sp.score( 'text.html source.php - string', reference_scope )
    ipdb.set_trace() 
    print 0 != sp.score( 'text.html source.php - ruby', reference_scope ) 
    
    ipdb.set_trace()
    print  sp.score( 'string', reference_scope ) > sp.score( 'source.php', reference_scope )
    ipdb.set_trace() 
    print sp.score( 'string.quoted', reference_scope ) > sp.score( 'source.php', reference_scope )
    ipdb.set_trace() 
    print sp.score( 'text source string', reference_scope ) > sp.score( 'source string', reference_scope )

if __name__ == '__main__':
    import ipdb

    python = parse_file('../../prymatex/resources/Bundles/Python.tmbundle/Syntaxes/Python.tmLanguage', 'python')
    p = TMDebugSyntaxProcessor()
    print python.parse(open('./syntax.py', 'r').read(), p)
    ipdb.set_trace()
    