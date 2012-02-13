#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

from prymatex.ui.support.editor import Ui_BundleEditor
from prymatex.gui.support import widgets


class PMXBundleEditor(QtGui.QDialog, Ui_BundleEditor):
    def __init__(self, application):
        super(PMXBundleEditor, self).__init__()
        self.setupUi(self)
        self.application = application
        self.manager = self.application.supportManager
        self.finished.connect(self.on_bundleEditor_finished)
        
        #Cargar los widgets editores
        self.configEditorWidgets()
        
        #Configurar filter, tree, toolbar y activaciones
        self.configSelectTop()
        self.configTreeView()
        self.configToolbar()
        self.configActivation()

    def on_bundleEditor_finished(self, code):
        self.saveChanges()
    
    #==========================================================
    # exec the dialog Show
    #==========================================================
    def exec_(self):
        #TODO: Mejorar esto porque se dispara con los filtros del proxy, quiza pegandole al modelo real o al manager
        self.manager.bundleTreeModel.rowsInserted.connect(self.on_bundleTreeModel_rowsInserted)
        value = QtGui.QDialog.exec_(self)
        self.manager.bundleTreeModel.rowsInserted.disconnect(self.on_bundleTreeModel_rowsInserted)
        return value
        
    def execEditor(self, typeFilter = "", namespaceFilter = ""):
        self.proxyTreeModel.setFilterNamespace(namespaceFilter)
        self.proxyTreeModel.setFilterBundleItemType(typeFilter)
        index = self.comboBoxItemFilter.findData(typeFilter)
        self.comboBoxItemFilter.setCurrentIndex(index)
        self.exec_()
        
    def execCommand(self):
        return self.execEditor("command")
    
    def execLanguage(self):
        return self.execEditor("syntax")
    
    def execSnippet(self):
        return self.execEditor("snippet")

    def configEditorWidgets(self):
        self.stackedWidget = QtGui.QStackedWidget()
        self.stackedWidget.setFrameShape(QtGui.QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.editorsLayout.insertWidget(1, self.stackedWidget)
        self.indexes = {}
        self.editors = [ widgets.PMXSnippetWidget(self),
                         widgets.PMXCommandWidget(self),
                         widgets.PMXDragCommandWidget(self),
                         widgets.PMXBundleWidget(self),
                         widgets.PMXTemplateFileWidget(self),
                         widgets.PMXTemplateWidget(self),
                         widgets.PMXPreferenceWidget(self),
                         widgets.PMXLanguageWidget(self),
                         widgets.PMXMacroWidget(self),
                         widgets.PMXEditorBaseWidget(self) ]
        for editor in self.editors:
            self.indexes[editor.TYPE] = self.stackedWidget.addWidget(editor)
        self.setCurrentEditor(self.editors[-1])
        
    #==========================================================
    # Toolbar
    #==========================================================
    def getBundleForIndex(self, index):
        if not index.isValid():
            return self.manager.getDefaultBundle()
        bundle = self.proxyTreeModel.node(index)
        while bundle.TYPE != 'bundle':
            bundle = bundle.parent
        return bundle
    
    def createBundleItem(self, itemName, itemType):
        index = self.treeView.currentIndex()
        bundle = self.getBundleForIndex(index)
        self.manager.createBundleItem(itemName, itemType, bundle)
        
    def on_actionCommand_triggered(self):
        self.createBundleItem(u"untitled", "command")
        
    def on_actionDragCommand_triggered(self):
        self.createBundleItem(u"untitled", "dragcommand")
        
    def on_actionLanguage_triggered(self):
        self.createBundleItem(u"untitled", "syntax")
        
    def on_actionSnippet_triggered(self):
        self.createBundleItem(u"untitled", "snippet")
        
    def on_actionTemplate_triggered(self):
        self.createBundleItem(u"untitled", "template")
        
    def on_actionTemplateFile_triggered(self):
        index = self.treeView.currentIndex()
        if index.isValid():
            template = self.proxyTreeModel.node(index)
            if template.TYPE == 'templatefile':
                template = template.parent
        self.manager.createTemplateFile(u"untitled", template)

    def on_actionPreferences_triggered(self):
        self.createBundleItem(u"untitled", "preference")

    def on_actionBundle_triggered(self):
        self.manager.createBundle("untitled")

    @QtCore.pyqtSlot()
    def on_pushButtonRemove_pressed(self):
        index = self.treeView.currentIndex()
        if index.isValid():
            item = self.proxyTreeModel.node(index)
            if item.TYPE == 'bundle':
                self.manager.deleteBundle(item)
            elif item.TYPE == 'templatefile':
                self.manager.deleteBundle(u"untitled", template)
            else:
                self.manager.deleteBundleItem(item)

    @QtCore.pyqtSlot()
    def on_pushButtonFilter_pressed(self):
        self.bundleFilterDialog.show()

    def configToolbar(self):
        self.toolbarMenu = QtGui.QMenu("Menu", self)
        action = QtGui.QAction("New Command", self)
        action.triggered.connect(self.on_actionCommand_triggered)
        self.toolbarMenu.addAction(action)
        action = QtGui.QAction("New Drag Command", self)
        action.triggered.connect(self.on_actionDragCommand_triggered)
        self.toolbarMenu.addAction(action)
        action = QtGui.QAction("New Language", self)
        action.triggered.connect(self.on_actionLanguage_triggered)
        self.toolbarMenu.addAction(action)
        action = QtGui.QAction("New Snippet", self)
        action.triggered.connect(self.on_actionSnippet_triggered)
        self.toolbarMenu.addAction(action)
        action = QtGui.QAction("New Template", self)
        action.triggered.connect(self.on_actionTemplate_triggered)
        self.toolbarMenu.addAction(action)
        self.templateFileAction = QtGui.QAction("New Template File", self)
        self.templateFileAction.triggered.connect(self.on_actionTemplateFile_triggered)
        self.toolbarMenu.addAction(self.templateFileAction)
        action = QtGui.QAction("New Preferences", self)
        action.triggered.connect(self.on_actionPreferences_triggered)
        self.toolbarMenu.addAction(action)
        self.toolbarMenu.addSeparator()
        action = QtGui.QAction("New Bundle", self)
        action.triggered.connect(self.on_actionBundle_triggered)
        self.toolbarMenu.addAction(action)
        
        def conditionalEnabledTemplateFile():
            node = self.proxyTreeModel.node(self.treeView.currentIndex())
            self.templateFileAction.setEnabled(not node.isRootNode() and (node.TYPE == "template" or node.TYPE == "templatefile"))
        self.toolbarMenu.aboutToShow.connect(conditionalEnabledTemplateFile)
        
        self.pushButtonAdd.setMenu(self.toolbarMenu)
        self.bundleFilterDialog = PMXBundleFilter(self)

    #==========================================================
    # Filter Top Bar
    #==========================================================
    @QtCore.pyqtSlot(int)
    def on_comboBoxItemFilter_activated(self, index):
        value = self.comboBoxItemFilter.itemData(index)
        self.proxyTreeModel.setFilterBundleItemType(value)
    
    def configSelectTop(self):
        self.comboBoxItemFilter.addItem("Show all", "")
        self.comboBoxItemFilter.addItem(QtGui.QIcon(":/icons/bundles/languages.png"), "Languages", "syntax")
        self.comboBoxItemFilter.addItem(QtGui.QIcon(":/icons/bundles/snippets.png"), "Snippets", "snippet")
        self.comboBoxItemFilter.addItem(QtGui.QIcon(":/icons/bundles/macros.png"), "Macros", "macro")
        self.comboBoxItemFilter.addItem(QtGui.QIcon(":/icons/bundles/commands.png"), "Commands", "command")
        self.comboBoxItemFilter.addItem(QtGui.QIcon(":/icons/bundles/drag-commands.png"), "DragCommands", "dragcommand")
        self.comboBoxItemFilter.addItem(QtGui.QIcon(":/icons/bundles/preferences.png"), "Preferences", "preference")
        self.comboBoxItemFilter.addItem(QtGui.QIcon(":/icons/bundles/templates.png"), "Templates", "template templatefile")
    
    #==========================================================
    # Tree View
    #==========================================================
    def getEditorForTreeItem(self, treeItem):
        if treeItem.TYPE in self.indexes:
            index = self.indexes[treeItem.TYPE]
            return self.editors[index]

    def on_bundleTreeModel_rowsInserted(self, parent, start, end):
        sIndex = self.manager.bundleTreeModel.index(start, 0, parent)
        index = self.proxyTreeModel.mapFromSource(sIndex)
        node = self.proxyTreeModel.node(index)
        self.treeView.setCurrentIndex(index)
        self.editTreeItem(node)
        self.treeView.edit(index)

    def on_proxyTreeModel_dataChanged(self, sindex, eindex):
        current = self.stackedWidget.currentWidget()
        self.labelTitle.setText(current.title)
        
    def on_treeView_Activated(self, index):
        treeItem = self.proxyTreeModel.node(index)
        self.editTreeItem(treeItem)

    def configTreeView(self, manager = None):
        self.proxyTreeModel = self.manager.bundleProxyTreeModel
        self.proxyTreeModel.dataChanged.connect(self.on_proxyTreeModel_dataChanged)
        
        self.treeView.setModel(self.proxyTreeModel)
        self.treeView.setHeaderHidden(True)
        self.treeView.setAnimated(True)
        self.treeView.activated.connect(self.on_treeView_Activated)
        self.treeView.pressed.connect(self.on_treeView_Activated)

    #===========================================================
    # Activation
    #===========================================================
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj == self.lineKeyEquivalentActivation:
            keyseq = int(event.modifiers()) + event.key()
            self.stackedWidget.currentWidget().setKeyEquivalent(keyseq)
            self.lineKeyEquivalentActivation.setText(QtGui.QKeySequence(keyseq).toString())
            return True
        return super(PMXBundleEditor, self).eventFilter(obj, event)
    
    @QtCore.pyqtSlot(int)
    def on_comboBoxActivation_currentIndexChanged(self, index):
        self.lineKeyEquivalentActivation.setVisible(index == 0)
        self.lineTabTriggerActivation.setVisible(index == 1)
    
    @QtCore.pyqtSlot(str)
    def on_lineEditScope_textEdited(self, text):
        self.stackedWidget.currentWidget().setScope(text)
    
    @QtCore.pyqtSlot(str)
    def on_lineTabTriggerActivation_textEdited(self, text):
        self.stackedWidget.currentWidget().setTabTrigger(text)
    
    def configActivation(self):
        self.comboBoxActivation.addItem("Key Equivalent")
        self.comboBoxActivation.addItem("Tab Trigger")
        self.lineKeyEquivalentActivation.installEventFilter(self)
    
    def saveChanges(self):
        #TODO: ver si tengo que guardar el current editor
        current = self.stackedWidget.currentWidget()
        if current.isChanged:
            if current.TYPE != "":
                if current.TYPE == "bundle":
                    self.manager.updateBundle(current.bundleItem, **current.changes)
                elif current.TYPE == "templatefile":
                    self.manager.updateTemplateFile(current.bundleItem, **current.changes)
                else:
                    self.manager.updateBundleItem(current.bundleItem, **current.changes)

    def editTreeItem(self, treeItem):
        self.saveChanges()
        editor = self.getEditorForTreeItem(treeItem)
        if editor != None:
            editor.edit(treeItem)
            self.setCurrentEditor(editor)

    def setCurrentEditor(self, editor):
        self.stackedWidget.setCurrentWidget(editor)
        self.labelTitle.setText(editor.title)
        scope = editor.getScope()
        tabTrigger = editor.getTabTrigger()
        keyEquivalent = editor.getKeyEquivalent()
        self.lineEditScope.setEnabled(scope is not None)
        self.lineKeyEquivalentActivation.setEnabled(keyEquivalent is not None)
        self.lineTabTriggerActivation.setEnabled(tabTrigger is not None)
        self.comboBoxActivation.setEnabled(tabTrigger is not None or keyEquivalent is not None)
        if scope is not None:
            self.lineEditScope.setText(scope)
        else:
            self.lineEditScope.clear()
        if not keyEquivalent and not tabTrigger:
            self.lineKeyEquivalentActivation.clear()
            self.lineTabTriggerActivation.clear()
            self.comboBoxActivation.setCurrentIndex(0)
            self.lineTabTriggerActivation.setVisible(False)
        else:
            if keyEquivalent is not None:
                self.lineKeyEquivalentActivation.setText(QtGui.QKeySequence(keyEquivalent).toString())
            if tabTrigger is not None:
                self.lineTabTriggerActivation.setText(tabTrigger)
            index = 0 if keyEquivalent else 1
            self.comboBoxActivation.setCurrentIndex(index)

from prymatex.utils.i18n import ugettext as _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class PMXBundleFilter(QtGui.QDialog):
    def __init__(self, bundleEditor):
        super(PMXBundleFilter, self).__init__(bundleEditor)
        self.setupUi(self)
        self.manager = bundleEditor.application.supportManager
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.proxy = QtGui.QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self.manager.bundleProxyModel)
        self.tableBundleItems.setModel(self.proxy)
        self.tableBundleItems.resizeColumnsToContents()
        self.tableBundleItems.resizeRowsToContents()
        
    def setupUi(self, BundleFilter):
        BundleFilter.setObjectName(_fromUtf8("BundleFilter"))
        BundleFilter.resize(330, 400)
        BundleFilter.setMinimumSize(QtCore.QSize(330, 400))
        self.verticalLayout = QtGui.QVBoxLayout(BundleFilter)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableBundleItems = QtGui.QTableView(BundleFilter)
        self.tableBundleItems.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableBundleItems.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableBundleItems.setShowGrid(False)
        self.tableBundleItems.setObjectName(_fromUtf8("tableBundleItems"))
        self.tableBundleItems.horizontalHeader().setVisible(False)
        self.tableBundleItems.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableBundleItems)
        self.labelHelp = QtGui.QLabel(BundleFilter)
        self.labelHelp.setWordWrap(True)
        self.labelHelp.setObjectName(_fromUtf8("labelHelp"))
        self.verticalLayout.addWidget(self.labelHelp)
        self.retranslateUi(BundleFilter)

    def retranslateUi(self, BundleFilter):
        BundleFilter.setWindowTitle(_('Enable/Disable Bundles'))
        self.labelHelp.setText(_('You should keep the Source, Text and TextMate bundles enabled, as these provide base functionality relied upon by other bundles.'))