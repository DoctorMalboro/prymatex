#!/usr/bin/env python
# -*- coding: utf-8 -*-

from prymatex.qt import QtCore, QtGui

from prymatex.core import PMXBaseWidgetComponent

from prymatex.ui.dialogs.treewidget import Ui_TreeWidgetDialog
from prymatex.models.projects import PropertyTreeNode, PropertiesProxyModel
from prymatex.models.configure import ConfigureTreeModel

class PMXProxyPropertyTreeNode(QtGui.QWidget, PropertyTreeNode):
    def __init__(self, name, parent):
        QtGui.QWidget.__init__(self)
        PropertyTreeNode.__init__(self, name, parent)

    def acceptFileSystemItem(self, fileSystemItem):
        return True
        
    def edit(self, fileSystemItem):
        pass

class PMXPropertiesDialog(QtGui.QDialog, Ui_TreeWidgetDialog, PMXBaseWidgetComponent):
    """Properties dialog, it's hold by the project docker"""
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        PMXBaseWidgetComponent.__init__(self)
        self.setupUi(self)
        
        self.baseWindowTitle = self.windowTitle()
        
        self.model = ConfigureTreeModel(self)
        self.model.proxyConfigureCreated.connect(self.on_model_proxyConfigureCreated)
        
        self.proxyModelProperties = PropertiesProxyModel(self)
        self.proxyModelProperties.setSourceModel(self.model)
        
        self.treeView.setModel(self.proxyModelProperties)
        
        self.stackedWidget = QtGui.QStackedWidget(self.splitter)
        self.widgetsLayout.addWidget(self.stackedWidget)
    
    def selectFirstIndex(self):
        firstIndex = self.proxyModelProperties.index(0, 0)
        rect = self.treeView.visualRect(firstIndex)
        self.treeView.setSelection(rect, QtGui.QItemSelectionModel.ClearAndSelect)
        treeNode = self.proxyModelProperties.node(firstIndex)
        self.setCurrentPropertyWidget(treeNode)

    def on_model_proxyConfigureCreated(self, proxyWidget):
        self.stackedWidget.addWidget(proxyWidget)
        
    def on_lineEditFilter_textChanged(self, text):
        self.proxyModelProperties.setFilterRegExp(QtCore.QRegExp(text, QtCore.Qt.CaseInsensitive))
        self.selectFirstIndex()
    
    def on_treeView_pressed(self, index):
        treeNode = self.proxyModelProperties.node(index)
        self.setCurrentPropertyWidget(treeNode)
        
    def on_treeView_activated(self, index):
        treeNode = self.proxyModelProperties.node(index)
        self.setCurrentPropertyWidget(treeNode)
    
    def setCurrentPropertyWidget(self, widget):
        widget.edit(self.proxyModelProperties.fileSystemItem)
        self.stackedWidget.setCurrentWidget(widget)
        self.textLabelTitle.setText(widget.title())
        self.textLabelPixmap.setPixmap(widget.icon().pixmap(20, 20))
        self.setWindowTitle("%s - %s" % (self.baseWindowTitle, widget.title()))
    
    def register(self, widget):
        index = self.stackedWidget.addWidget(widget)
        self.model.addConfigNode(widget)
    
    def exec_(self, fileSystemItem):
        self.proxyModelProperties.setFilterFileSystem(fileSystemItem)
        self.selectFirstIndex()
        return QtGui.QDialog.exec_(self)
        
