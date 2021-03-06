#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from copy import copy

from prymatex.qt import QtGui, QtCore

from prymatex.gui.codeeditor.processors import PMXSyntaxProcessor
from prymatex.gui.codeeditor.userdata import PMXBlockUserData
from prymatex.support.syntax import PMXSyntax
from prymatex.utils.decorators.helpers import printtime

#TODO: Usar mas el modulo de string en general, string.punctuation, mover las regexp a otro lugar, recursos quiza?

RE_WORD = re.compile(r"([A-Za-z_]\w+\b)", re.UNICODE)
RE_WHITESPACE = re.compile(r'^(?P<whitespace>\s+)', re.UNICODE)

def whiteSpace(text):
    match = RE_WHITESPACE.match(text)
    try:
        ws = match.group('whitespace')
        return ws
    except AttributeError:
        return ''

class PMXSyntaxHighlighter(QtGui.QSyntaxHighlighter):
    NO_STATE = -1
    SINGLE_LINE = 1
    FORMAT_CACHE = {}
    highlightReady = QtCore.pyqtSignal()
    
    def __init__(self, editor, syntax = None, theme = None):
        QtGui.QSyntaxHighlighter.__init__(self, editor)
        self.editor = editor
        self.processor = PMXSyntaxProcessor(editor)
        self.syntax = syntax
        self.theme = theme
        
        #Highlight Function
        self.highlight_function = self.realtime_highlight
        self.highlightTask = self.editor.application.scheduler.idleTask()

        #Conect signals
        self.editor.afterOpen.connect(self.on_editor_afterOpen)

    def on_editor_afterOpen(self):
        #Cuidado si estoy corriendo la tarea no correrla nuevamente
        if not self.highlightTask.isRunning():
            self.highlight_function = self.async_highlight
            self.highlightTask = self.editor.application.scheduler.newTask(self.highlightAllDocument())
            def on_highlightReady():
                #Restore realitme function
                self.highlight_function = self.realtime_highlight
                self.highlightReady.emit()
            self.highlightTask.done.connect(on_highlightReady)

    @property
    def ready(self):
        if self.theme and self.syntax:
            self.setDocument(self.editor.document())
            return True
        return False
    
    def setSyntax(self, syntax):
        if self.highlightTask.isRunning():
            self.highlightTask.cancel()
        self.syntax = syntax
        if self.ready:
            self.on_editor_afterOpen()
        
    def setTheme(self, theme):
        PMXSyntaxHighlighter.FORMAT_CACHE = {}
        self.theme = theme
        if self.ready:
            self.rehighlight()
    
    def hasTheme(self):
        return self.theme is not None
            
    def highlightAllDocument(self):
        block = self.document().begin()
        self.processor.startParsing(self.syntax.scopeName)
        stack = [[self.syntax.grammar, None]]
        while block.isValid():
            text = block.text()
            self.syntax.parseLine(stack, text, self.processor)
            userData = block.userData()
            if userData is None:
                userData = PMXBlockUserData()
                block.setUserData(userData)
            
            self.setupBlockUserData(text, block, userData)
            
            blockState = len(stack)
            if blockState != self.SINGLE_LINE:
                userData.setProcessorState((copy(stack), copy(self.processor.scopes())))
            userData.textHash = hash(text) + hash(self.syntax.scopeName) + blockState
            block.setUserState(blockState)
            
            self.rehighlightBlock(block)
            block = block.next()
            yield
        self.processor.endParsing(self.syntax.scopeName)
        
    def setupBlockUserData(self, text, block, userData):
        userData.setRanges(self.processor.scopeRanges)
        userData.setChunks(self.processor.lineChunks)
        userData.blank = text.strip() == ""
        # TODO UserDataProcessors?
        #1 Update words
        if userData.words != self.processor.words:
            self.editor.updateWords(block, userData, self.processor.words)
     
        #2 Update Indent
        indent = whiteSpace(text)
        if indent != userData.indent:
            userData.indent = indent
            self.editor.updateIndent(block, userData, indent)

        #3 Update Folding
        foldingMark = self.syntax.folding(text)
        if userData.foldingMark != foldingMark:
            userData.foldingMark = foldingMark
            self.editor.updateFolding(block, userData, foldingMark)
            
        #4 Update Symbols
        symbolRange = filter(lambda ((start, end), p): p.showInSymbolList, 
            map(lambda ((start, end), scope): ((start, end), self.editor.preferenceSettings(scope)), userData.scopeRanges()))
        if symbolRange:
            #TODO: Hacer la transformacion de los symbolos
            #symbol = text[symbolRange[0][1]:symbolRange[-1][2]]
            #symbol = symbolRange[0][0].transformSymbol(symbol)
            symbol = text
        else:
            symbol = None

        if userData.symbol != symbol:
            userData.symbol = symbol
            self.editor.updateSymbol(block, userData, symbol)

    def highlightBlock(self, text):
        self.highlight_function(text)
        
    def async_highlight(self, text):
        userData = self.currentBlock().userData()
        if userData:
            self.applyFormat(userData)
    
    def realtime_highlight(self, text):
        userData = self.currentBlock().userData()
        if userData is not None and userData.textHash == hash(text) + hash(self.syntax.scopeName) + self.previousBlockState():
            self.applyFormat(userData)
        else:
            self.processor.startParsing(self.syntax.scopeName)
            if self.previousBlockState() not in [self.SINGLE_LINE, self.NO_STATE]:
                #Recupero una copia del stack y los scopes del user data
                stack, scopes = self.currentBlock().previous().userData().processorState()
                #Set copy, not original
                stack = stack[:]
                self.processor.setScopes(scopes[:])
            else:
                #Creo un stack y scopes nuevos
                stack = [[self.syntax.grammar, None]]

            # A parserar mi amor, vamos a parsear mi amor
            self.syntax.parseLine(stack, text, self.processor)
            self.processor.endParsing(self.syntax.scopeName)

            if userData is None:
                userData = PMXBlockUserData()
                self.setCurrentBlockUserData(userData)

            self.setupBlockUserData(text, self.currentBlock(), userData)

            blockState = len(stack)
            
            if blockState != self.SINGLE_LINE:
                userData.setProcessorState((copy(stack), copy(self.processor.scopes())))
            userData.textHash = hash(text) + hash(self.syntax.scopeName) + blockState
            
            self.setCurrentBlockState(blockState)
            self.applyFormat(userData)

    def applyFormat(self, userData):
        for (start, end), scopeHash in userData.scopeRanges():
            format = self.highlightFormat(self.editor.scopeName(scopeHash))
            if format is not None:
                self.setFormat(start, end - start, format)

    def highlightFormat(self, scope):
        if self.theme is None:
            return None
        if scope not in PMXSyntaxHighlighter.FORMAT_CACHE:
            format = QtGui.QTextCharFormat()
            settings = self.theme.getStyle(scope)
            if 'foreground' in settings:
                format.setForeground(settings['foreground'])
            if 'background' in settings:
                format.setBackground(settings['background'])
            if 'fontStyle' in settings:
                if 'bold' in settings['fontStyle']:
                    format.setFontWeight(QtGui.QFont.Bold)
                if 'underline' in settings['fontStyle']:
                    format.setFontUnderline(True)
                if 'italic' in settings['fontStyle']:
                    format.setFontItalic(True)
            PMXSyntaxHighlighter.FORMAT_CACHE[scope] = format 
        return PMXSyntaxHighlighter.FORMAT_CACHE[scope]