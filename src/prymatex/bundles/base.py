#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re, plistlib
from glob import glob
from copy import deepcopy
from xml.parsers.expat import ExpatError

# for run as main
if __name__ == "__main__":
    import sys
    sys.path.append(os.path.abspath('../..'))
from prymatex.bundles.score import PMXScoreManager
from prymatex.core.config import settings
from prymatex.bundles.qtadapter import buildKeyEquivalentPattern, buildKeySequence

'''
    Este es el unico camino -> http://manual.macromates.com/en/
    http://manual.macromates.com/en/bundles
    http://blog.macromates.com/2005/introduction-to-scopes/
    http://manual.macromates.com/en/scope_selectors.html
'''

RE_XML_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + \
                 u'|' + \
                 u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % \
                  (unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
                   unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff),
                   unichr(0xd800),unichr(0xdbff),unichr(0xdc00),unichr(0xdfff))

RE_XML_ILLEGAL = re.compile(RE_XML_ILLEGAL)

class PMXMenuNode(object):
    MENU_SPACE = '-' * 36
    def __init__(self, name = '', items = [], excludedItems = [], submenus = {}):
        self.name = name
        self.items = items
        self.excludedItems = excludedItems
        self.main = dict(map(lambda i: (i, None), filter(lambda x: x != self.MENU_SPACE, self.items)))
        for uuid, submenu in submenus.iteritems():
            self[uuid] = PMXMenuNode(**submenu)

    def __contains__(self, key):
        return key in self.main or any(map(lambda submenu: key in submenu, filter(lambda x: isinstance(x, PMXMenuNode), self.main.values())))

    def __getitem__(self, key):
        try:
            return self.main[key]
        except KeyError:
            for submenu in filter(lambda x: isinstance(x, PMXMenuNode), self.main.values()):
                if key in submenu:
                    return submenu[key]
        raise KeyError(key)
    
    def __setitem__(self, key, menu):
        if key in self.main:
            self.main[key] = menu
        else:
            for submenu in filter(lambda x: isinstance(x, PMXMenuNode), self.main.values()):
                if key in submenu:
                    submenu[key] = menu

    def iteritems(self):
        items = self.items
        if self.excludedItems:
            items = filter(lambda x: not x in self.excludedItems, items)
        for item in items:
            if item != self.MENU_SPACE:
                yield (item, self[item])
            else:
                yield (self.MENU_SPACE, self.MENU_SPACE)

class PMXBundle(object):
    BUNDLES = {}
    TAB_TRIGGERS = {}
    KEY_EQUIVALENTS = {}
    PREFERENCES = {}
    scores = PMXScoreManager()
    
    def __init__(self, hash, path):
        for key in [    'uuid', 'name', 'deleted', 'ordering', 'mainMenu', 'contactEmailRot13', 'description', 'contactName' ]:
            value = hash.pop(key, None)
            if key == 'mainMenu' and value != None:
                value = PMXMenuNode(self.name, **value)
            setattr(self, key, value)
        self.path = path
        self.syntaxes = []
        self.snippets = []
        self.macros = []
        self.commands = []
        self.preferences = []
        
        if hash:
            print "Bundle '%s' has more values (%s)" % (self.name, ', '.join(hash.keys()))

    def addItem(self, item):
        if self.mainMenu != None:
            self.mainMenu[item.uuid] = item
        if item.tabTrigger != None:
            PMXBundle.TAB_TRIGGERS.setdefault(item.tabTrigger, []).append(item)
        if item.keyEquivalent != None:
            PMXBundle.KEY_EQUIVALENTS.setdefault(item.keyEquivalent, []).append(item)
        # I'm four father
        item.bundle = self

    def addSyntax(self, syntax):
        self.addItem(syntax)
        self.syntaxes.append(syntax)

    def addSnippet(self, snippet):
        self.addItem(snippet)
        self.snippets.append(snippet)

    def addMacro(self, macro):
        self.addItem(macro)
        self.macros.append(macro)

    def addCommand(self, command):
        self.addItem(command)
        self.commands.append(command)

    def addPreference(self, preference):
        self.addItem(preference)
        self.preferences.append(preference)
        PMXBundle.PREFERENCES.setdefault(preference.scope, []).append(preference)
    
    def getSyntaxByName(self, name):
        for syntax in self.syntaxes:
            if syntax.name == name:
                return syntax

    def getBundleSupportPath(self):
        return os.path.join(self.path, 'Support')

    @staticmethod
    def loadBundle(path, elements, name_space = 'prymatex'):
        info_file = os.path.join(path, 'info.plist')
        try:
            data = plistlib.readPlist(info_file)
            bundle = PMXBundle(data, path)
        except Exception, e:
            print "Error in bundle %s (%s)" % (info_file, e)
        
        #Disabled?
        if bundle.uuid in settings.disabled_bundles:
            return
        
        for name, pattern, klass in elements:
            files = glob(os.path.join(path, pattern))
            for sf in files:
                try:
                    data = plistlib.readPlist(sf)
                except Exception, e:
                    data = open(sf).read()
                    for match in RE_XML_ILLEGAL.finditer(data):
                        data = data[:match.start()] + "?" + data[match.end():]
                    try:
                        data = plistlib.readPlistFromString(data)
                    except ExpatError, e:
                        print "Error in %s for %s (%s)" % (klass.__name__, sf, e)
                        continue;
                try:
                    item = klass(data, name_space)
                    method = getattr(bundle, "add" + name, None)
                    if method != None:
                        method(item)
                except Exception, e:
                    print "Error in %s for %s (%s)" % (klass.__name__, sf, e)
        PMXBundle.BUNDLES[bundle.uuid] = bundle
        return bundle

    @classmethod
    def getBundleByName(cls, name):
        for uuid, bundle in cls.BUNDLES.iteritems():
            if bundle.name == name:
                return bundle

    @classmethod
    def getPreferences(cls, scope):
        preferences = []
        for key in cls.PREFERENCES.keys():
            if key == None:
                score = 1
            else:
                score = cls.scores.score(scope, key)
            if score != 0:
                preferences.append((score, cls.PREFERENCES[key]))
        preferences.sort(key = lambda t: t[0])
        result = []
        for _, ps in preferences:
            result.extend(ps)
        return result

    @classmethod
    def getTabTriggerItem(cls, keyword, scope):
        items = []
        if cls.TAB_TRIGGERS.has_key(keyword):
            for item in cls.TAB_TRIGGERS[keyword]:
                if not item.ready():
                    item.compile()
                #score = cls.scores.score(scope, item.scope)
                score = cls.scores.score(item.scope, scope)
                if score != 0:
                    items.append((score, item))
            items.sort(key = lambda t: t[0])
            items = map(lambda (score, item): item.clone(), items)
        return items
            
    @classmethod
    def getKeyEquivalentItem(cls, key_event, scope):
        items = []
        key = buildKeyEquivalentPattern(key_event)
        print key
        if cls.KEY_EQUIVALENTS.has_key(key):
            for item in cls.KEY_EQUIVALENTS[key]:
                if not item.ready():
                    item.compile()
                score = cls.scores.score(item.scope, scope)
                #score = cls.scores.score(scope, item.scope)
                if score != 0:
                    items.append((score, item))
            items.sort(key = lambda t: t[0])
            items = map(lambda (score, item): item.clone(), items)
        return items

class PMXBundleItem(object):
    def __init__(self, hash, name_space):
        self.hash = deepcopy(hash)
        self.name_space = name_space
        for key in [    'uuid', 'bundleUUID', 'name', 'tabTrigger', 'keyEquivalent', 'scope' ]:
            setattr(self, key, hash.pop(key, None))
    
    def getKeySequence(self):
        if self.keyEquivalent != None:
            return buildKeySequence(self.keyEquivalent)
    
    def clone(self):
        return self
    
    def ready(self):
        return True
    
    def compile(self):
        pass
    
    def resolve(self, indentation, tabreplacement, environment):
        pass
#----------------------------------------
# Tests
#----------------------------------------
def test_preferences():
    from prymatex.bundles.preference import PMXPreference
    bundle = PMXBundle.getBundleByName('Python')
    print PMXPreference.getSettings(bundle.getPreferences('source.python'))

def test_snippets():
    #bundle = PMXBundle.getBundleByName('LaTeX')
    bundle = PMXBundle.getBundleByName('Python')
    #bundle = PMXBundle.getBundleByName('C')
    for snippet in bundle.snippets:
        #if snippet.name.startswith("Itemize Lines"):
        #if snippet.name.startswith("Sub Sub"):
            print snippet.name
            snippet.compile()
            snippet.resolve("", "    ", {"TM_CURRENT_LINE": "  ", "TM_SCOPE": "text.tex.latex string.other.math.block.environment.latex"})
            print "-" * 15, " Test ", snippet.name, " (", snippet.tabTrigger, ") ", "-" * 15
            print "Origin: ", len(snippet), snippet.next()
            print snippet, snippet.ends
            clon = snippet.clone()
            clon.write(0, "Foo")
            clon.write(1, "Bar %d algo %n pepe %s")
            clon.write(3, "bar, foo, bar")
            print "Clone: ", len(clon), clon.next()
            print clon, clon.ends
            
def print_snippet_syntax():
    bundle = PMXBundle.getBundleByName('Bundle Development')
    syntax = bundle.getSyntaxByName("Snippet")
    pprint(syntax.hash)
    
def test_syntaxes():
    from prymatex.bundles.syntax import PMXSyntax
    from prymatex.bundles.processor import PMXDebugSyntaxProcessor
    syntax = PMXSyntax.getSyntaxesByName("LaTeX")
    syntax[0].parse("item", PMXDebugSyntaxProcessor())
    print PMXSyntax.getSyntaxesNames()

def print_commands():
    from pprint import pprint
    pprint(PMXBundle.KEY_EQUIVALENTS)
    
if __name__ == '__main__':
    from prymatex.bundles import BUNDLE_ELEMENTS
    from pprint import pprint
    for file in glob(os.path.join('../share/Bundles/', '*')):
        PMXBundle.loadBundle(file, BUNDLE_ELEMENTS)
    test_snippets()