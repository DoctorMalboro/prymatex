#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

from PyQt4 import QtCore, QtGui

from prymatex import resources
from prymatex.ui.dialogs.selector import Ui_SelectorDialog

class PMXSelectorDialog(QtGui.QDialog, Ui_SelectorDialog):
    '''
    This dialog allow the user to search through commands, snippets and macros in the current scope easily.
    An instance is hold in the main window and triggered with an action.
    '''
    def __init__(self, parent = None, title = "Select item"):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.lineFilter.installEventFilter(self)
        self.tableItems.installEventFilter(self)
        
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.proxy = QtGui.QSortFilterProxyModel(self)
        self.tableItems.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableItems.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.tableItems.verticalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
        self.tableItems.setModel(self.proxy)
        self.setWindowTitle(title)
    
    def createStandardItemModel(self, items):
        def dictToStandardItem(a_dict):
            item = QtGui.QStandardItem()
            item.setText(a_dict.get('title', ''))
            image = a_dict.get('image')
            if image is not None:
                if isinstance(image, QtGui.QIcon):
                    item.setIcon(image)
                else:
                    image = resources.getIcon(image) or QtGui.QIcon()
                item.setIcon(image)
            return item
        model = QtGui.QStandardItemModel(self)
        for row in items:
            items = map(dictToStandardItem, row)
            model.appendRow(items)
        return model
        
    def select(self, data):
        """
            @param items: List of rows, each row has a list of columns, and each column is a dict with "title", "image", "tooltip"
            @return: The selected index
        """
        self.index = None
        self.lineFilter.clear()
        self.lineFilter.setFocus()
        
        model = None
        if isinstance(data, collections.Iterable):
            model = self.createStandardItemModel(data)
        elif isinstance(data, QtCore.QAbstractItemModel):
            model = data
        else:
            raise Exception("No Data")
        self.proxy.setSourceModel(model)
        
        self.tableItems.selectRow(0)
        if self.exec_() == self.Accepted:
            return self.index
    
    def eventFilter(self, obj, event):
        '''Filters lineEdit key strokes to select model items'''
        if obj is self.lineFilter:
            if event.type() == QtCore.QEvent.KeyPress:
                key = event.key() 
                if key == QtCore.Qt.Key_Down:
                    self.tableItems.setFocus()
                    self.tableItems.event(event)
                    obj.setFocus()
                    return True
                elif key == QtCore.Qt.Key_Up:
                    self.tableItems.setFocus()
                    self.tableItems.event(event)
                    obj.setFocus()
                    return True
        elif obj is self.tableItems:
            if event.type() == QtCore.QEvent.KeyPress:
                self.lineFilter.setFocus()
                self.lineFilter.event(event)
                return True
        return QtGui.QWidget.eventFilter(self, obj, event)
            
    def on_lineFilter_textChanged(self, text):
        regexp = QtCore.QRegExp("*%s*" % text, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.Wildcard)
        self.proxy.setFilterRegExp(regexp)
        self.tableItems.selectRow(0)
        
    def on_tableItems_activated(self, index):
        sIndex = self.proxy.mapToSource(index)
        self.index = sIndex.row()
        self.accept()
        
    def on_tableItems_doubleClicked(self, index):
        sIndex = self.proxy.mapToSource(index)
        self.index = sIndex.row()
        self.accept()
    
    def on_lineFilter_returnPressed(self):
        indexes = self.tableItems.selectedIndexes()
        if indexes:
            sIndex = self.proxy.mapToSource(indexes[0])
            self.index = sIndex.row()
            self.accept()
