# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/mainwindow.ui'
#
# Created: Fri Dec  2 15:19:24 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from prymatex.utils.i18n import ugettext as _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(801, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/Prymatex_Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitTabWidget = PMXSplitTabWidget(self.centralwidget)
        self.splitTabWidget.setObjectName(_fromUtf8("splitTabWidget"))
        self.verticalLayout.addWidget(self.splitTabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuRecentFiles = QtGui.QMenu(self.menuFile)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/document-open-recent.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRecentFiles.setIcon(icon1)
        self.menuRecentFiles.setObjectName(_fromUtf8("menuRecentFiles"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuGutter = QtGui.QMenu(self.menuView)
        self.menuGutter.setObjectName(_fromUtf8("menuGutter"))
        self.menuFont = QtGui.QMenu(self.menuView)
        self.menuFont.setObjectName(_fromUtf8("menuFont"))
        self.menuPanels = QtGui.QMenu(self.menuView)
        self.menuPanels.setObjectName(_fromUtf8("menuPanels"))
        self.menuText = QtGui.QMenu(self.menubar)
        self.menuText.setObjectName(_fromUtf8("menuText"))
        self.menuConvert = QtGui.QMenu(self.menuText)
        self.menuConvert.setObjectName(_fromUtf8("menuConvert"))
        self.menuMove = QtGui.QMenu(self.menuText)
        self.menuMove.setObjectName(_fromUtf8("menuMove"))
        self.menuNavigation = QtGui.QMenu(self.menubar)
        self.menuNavigation.setObjectName(_fromUtf8("menuNavigation"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuSelect = QtGui.QMenu(self.menuEdit)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/edit-select-all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuSelect.setIcon(icon2)
        self.menuSelect.setObjectName(_fromUtf8("menuSelect"))
        self.menuBundles = QtGui.QMenu(self.menubar)
        self.menuBundles.setObjectName(_fromUtf8("menuBundles"))
        self.menuBundleEditor = QtGui.QMenu(self.menuBundles)
        self.menuBundleEditor.setObjectName(_fromUtf8("menuBundleEditor"))
        self.menuPreferences = QtGui.QMenu(self.menubar)
        self.menuPreferences.setObjectName(_fromUtf8("menuPreferences"))
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/document-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon3)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon4)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/document-save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon5)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSaveAs = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/document-save-as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon6)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionSaveAll = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/document-save-all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAll.setIcon(icon7)
        self.actionSaveAll.setObjectName(_fromUtf8("actionSaveAll"))
        self.actionClose = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/dialog-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon8)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionCloseOthers = QtGui.QAction(MainWindow)
        self.actionCloseOthers.setObjectName(_fromUtf8("actionCloseOthers"))
        self.actionQuit = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/application-exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon9)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionUndo = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/edit-undo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon10)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionRedo = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/edit-redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon11)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionCopy = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/edit-copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon12)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionCut = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/edit-cut.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon13)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionPaste = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/edit-paste.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon14)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionFind = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/edit-find.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon15)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionSettings = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/configure.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon16)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionFullscreen = QtGui.QAction(MainWindow)
        self.actionFullscreen.setCheckable(True)
        self.actionFullscreen.setObjectName(_fromUtf8("actionFullscreen"))
        self.actionShowMenus = QtGui.QAction(MainWindow)
        self.actionShowMenus.setCheckable(True)
        self.actionShowMenus.setObjectName(_fromUtf8("actionShowMenus"))
        self.actionZoomIn = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/resources/actions/zoom-in.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomIn.setIcon(icon17)
        self.actionZoomIn.setObjectName(_fromUtf8("actionZoomIn"))
        self.actionZoomOut = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/resources/actions/zoom-out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomOut.setIcon(icon18)
        self.actionZoomOut.setObjectName(_fromUtf8("actionZoomOut"))
        self.actionShowLineNumbers = QtGui.QAction(MainWindow)
        self.actionShowLineNumbers.setCheckable(True)
        self.actionShowLineNumbers.setObjectName(_fromUtf8("actionShowLineNumbers"))
        self.actionShowFolding = QtGui.QAction(MainWindow)
        self.actionShowFolding.setCheckable(True)
        self.actionShowFolding.setObjectName(_fromUtf8("actionShowFolding"))
        self.actionShowBookmarks = QtGui.QAction(MainWindow)
        self.actionShowBookmarks.setCheckable(True)
        self.actionShowBookmarks.setObjectName(_fromUtf8("actionShowBookmarks"))
        self.actionConvertToUppercase = QtGui.QAction(MainWindow)
        self.actionConvertToUppercase.setObjectName(_fromUtf8("actionConvertToUppercase"))
        self.actionConvertToLowercase = QtGui.QAction(MainWindow)
        self.actionConvertToLowercase.setObjectName(_fromUtf8("actionConvertToLowercase"))
        self.actionConvertToTitlecase = QtGui.QAction(MainWindow)
        self.actionConvertToTitlecase.setObjectName(_fromUtf8("actionConvertToTitlecase"))
        self.actionConvertToOppositeCase = QtGui.QAction(MainWindow)
        self.actionConvertToOppositeCase.setObjectName(_fromUtf8("actionConvertToOppositeCase"))
        self.actionConvertTranspose = QtGui.QAction(MainWindow)
        self.actionConvertTranspose.setObjectName(_fromUtf8("actionConvertTranspose"))
        self.actionConvertTabToSpaces = QtGui.QAction(MainWindow)
        self.actionConvertTabToSpaces.setObjectName(_fromUtf8("actionConvertTabToSpaces"))
        self.actionConvertSpacesToTabs = QtGui.QAction(MainWindow)
        self.actionConvertSpacesToTabs.setObjectName(_fromUtf8("actionConvertSpacesToTabs"))
        self.actionFilterThroughCommand = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/actions/view-filter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilterThroughCommand.setIcon(icon19)
        self.actionFilterThroughCommand.setObjectName(_fromUtf8("actionFilterThroughCommand"))
        self.actionExecute = QtGui.QAction(MainWindow)
        self.actionExecute.setObjectName(_fromUtf8("actionExecute"))
        self.actionToggleBookmark = QtGui.QAction(MainWindow)
        self.actionToggleBookmark.setObjectName(_fromUtf8("actionToggleBookmark"))
        self.actionNextBookmark = QtGui.QAction(MainWindow)
        self.actionNextBookmark.setObjectName(_fromUtf8("actionNextBookmark"))
        self.actionPreviousBookmark = QtGui.QAction(MainWindow)
        self.actionPreviousBookmark.setObjectName(_fromUtf8("actionPreviousBookmark"))
        self.actionRemoveAllBookmarks = QtGui.QAction(MainWindow)
        self.actionRemoveAllBookmarks.setObjectName(_fromUtf8("actionRemoveAllBookmarks"))
        self.actionNextTab = QtGui.QAction(MainWindow)
        self.actionNextTab.setObjectName(_fromUtf8("actionNextTab"))
        self.actionPreviousTab = QtGui.QAction(MainWindow)
        self.actionPreviousTab.setObjectName(_fromUtf8("actionPreviousTab"))
        self.actionReport_Bug = QtGui.QAction(MainWindow)
        self.actionReport_Bug.setObjectName(_fromUtf8("actionReport_Bug"))
        self.actionTranslate_this_application = QtGui.QAction(MainWindow)
        self.actionTranslate_this_application.setObjectName(_fromUtf8("actionTranslate_this_application"))
        self.actionProjectHomepage = QtGui.QAction(MainWindow)
        self.actionProjectHomepage.setObjectName(_fromUtf8("actionProjectHomepage"))
        self.actionTakeScreenshot = QtGui.QAction(MainWindow)
        self.actionTakeScreenshot.setObjectName(_fromUtf8("actionTakeScreenshot"))
        self.actionAbout_this_application = QtGui.QAction(MainWindow)
        self.actionAbout_this_application.setObjectName(_fromUtf8("actionAbout_this_application"))
        self.actionAboutQt = QtGui.QAction(MainWindow)
        self.actionAboutQt.setObjectName(_fromUtf8("actionAboutQt"))
        self.actionNewFromTemplate = QtGui.QAction(MainWindow)
        self.actionNewFromTemplate.setEnabled(True)
        self.actionNewFromTemplate.setObjectName(_fromUtf8("actionNewFromTemplate"))
        self.actionShowTabsAndSpaces = QtGui.QAction(MainWindow)
        self.actionShowTabsAndSpaces.setCheckable(True)
        self.actionShowTabsAndSpaces.setObjectName(_fromUtf8("actionShowTabsAndSpaces"))
        self.actionShowLineAndParagraphs = QtGui.QAction(MainWindow)
        self.actionShowLineAndParagraphs.setCheckable(True)
        self.actionShowLineAndParagraphs.setObjectName(_fromUtf8("actionShowLineAndParagraphs"))
        self.actionRead_documentation = QtGui.QAction(MainWindow)
        self.actionRead_documentation.setObjectName(_fromUtf8("actionRead_documentation"))
        self.actionSelectWord = QtGui.QAction(MainWindow)
        self.actionSelectWord.setObjectName(_fromUtf8("actionSelectWord"))
        self.actionSelectLine = QtGui.QAction(MainWindow)
        self.actionSelectLine.setObjectName(_fromUtf8("actionSelectLine"))
        self.actionSelectParagraph = QtGui.QAction(MainWindow)
        self.actionSelectParagraph.setObjectName(_fromUtf8("actionSelectParagraph"))
        self.actionSelectEnclosingBrackets = QtGui.QAction(MainWindow)
        self.actionSelectEnclosingBrackets.setObjectName(_fromUtf8("actionSelectEnclosingBrackets"))
        self.actionSelectCurrentScope = QtGui.QAction(MainWindow)
        self.actionSelectCurrentScope.setObjectName(_fromUtf8("actionSelectCurrentScope"))
        self.actionSelectAll = QtGui.QAction(MainWindow)
        self.actionSelectAll.setObjectName(_fromUtf8("actionSelectAll"))
        self.actionCloseAll = QtGui.QAction(MainWindow)
        self.actionCloseAll.setObjectName(_fromUtf8("actionCloseAll"))
        self.actionShowStatus = QtGui.QAction(MainWindow)
        self.actionShowStatus.setCheckable(True)
        self.actionShowStatus.setObjectName(_fromUtf8("actionShowStatus"))
        self.actionFindReplace = QtGui.QAction(MainWindow)
        self.actionFindReplace.setObjectName(_fromUtf8("actionFindReplace"))
        self.actionOpenAllRecentFiles = QtGui.QAction(MainWindow)
        self.actionOpenAllRecentFiles.setObjectName(_fromUtf8("actionOpenAllRecentFiles"))
        self.actionRemoveAllRecentFiles = QtGui.QAction(MainWindow)
        self.actionRemoveAllRecentFiles.setObjectName(_fromUtf8("actionRemoveAllRecentFiles"))
        self.actionShowBundleEditor = QtGui.QAction(MainWindow)
        self.actionShowBundleEditor.setObjectName(_fromUtf8("actionShowBundleEditor"))
        self.actionEditCommands = QtGui.QAction(MainWindow)
        self.actionEditCommands.setObjectName(_fromUtf8("actionEditCommands"))
        self.actionEditLanguages = QtGui.QAction(MainWindow)
        self.actionEditLanguages.setObjectName(_fromUtf8("actionEditLanguages"))
        self.actionEditSnippets = QtGui.QAction(MainWindow)
        self.actionEditSnippets.setObjectName(_fromUtf8("actionEditSnippets"))
        self.actionReloadBundles = QtGui.QAction(MainWindow)
        self.actionReloadBundles.setObjectName(_fromUtf8("actionReloadBundles"))
        self.actionSelectBundleItem = QtGui.QAction(MainWindow)
        self.actionSelectBundleItem.setObjectName(_fromUtf8("actionSelectBundleItem"))
        self.actionGoToLine = QtGui.QAction(MainWindow)
        self.actionGoToLine.setObjectName(_fromUtf8("actionGoToLine"))
        self.actionGoToTab = QtGui.QAction(MainWindow)
        self.actionGoToTab.setObjectName(_fromUtf8("actionGoToTab"))
        self.actionGoToSymbol = QtGui.QAction(MainWindow)
        self.actionGoToSymbol.setObjectName(_fromUtf8("actionGoToSymbol"))
        self.actionChooseTab = QtGui.QAction(MainWindow)
        self.actionChooseTab.setObjectName(_fromUtf8("actionChooseTab"))
        self.actionMoveLineUp = QtGui.QAction(MainWindow)
        self.actionMoveLineUp.setObjectName(_fromUtf8("actionMoveLineUp"))
        self.actionMoveLineDown = QtGui.QAction(MainWindow)
        self.actionMoveLineDown.setObjectName(_fromUtf8("actionMoveLineDown"))
        self.actionMoveColumnRight = QtGui.QAction(MainWindow)
        self.actionMoveColumnRight.setObjectName(_fromUtf8("actionMoveColumnRight"))
        self.actionMoveColumnLeft = QtGui.QAction(MainWindow)
        self.actionMoveColumnLeft.setObjectName(_fromUtf8("actionMoveColumnLeft"))
        self.menuRecentFiles.addAction(self.actionOpenAllRecentFiles)
        self.menuRecentFiles.addAction(self.actionRemoveAllRecentFiles)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionNewFromTemplate)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuRecentFiles.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionSaveAll)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionCloseAll)
        self.menuFile.addAction(self.actionCloseOthers)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuGutter.addAction(self.actionShowFolding)
        self.menuGutter.addAction(self.actionShowBookmarks)
        self.menuGutter.addAction(self.actionShowLineNumbers)
        self.menuFont.addAction(self.actionZoomIn)
        self.menuFont.addAction(self.actionZoomOut)
        self.menuView.addAction(self.menuPanels.menuAction())
        self.menuView.addAction(self.menuFont.menuAction())
        self.menuView.addAction(self.menuGutter.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionShowTabsAndSpaces)
        self.menuView.addAction(self.actionShowLineAndParagraphs)
        self.menuConvert.addAction(self.actionConvertToUppercase)
        self.menuConvert.addAction(self.actionConvertToLowercase)
        self.menuConvert.addAction(self.actionConvertToTitlecase)
        self.menuConvert.addAction(self.actionConvertToOppositeCase)
        self.menuConvert.addSeparator()
        self.menuConvert.addAction(self.actionConvertSpacesToTabs)
        self.menuConvert.addAction(self.actionConvertTabToSpaces)
        self.menuConvert.addSeparator()
        self.menuConvert.addAction(self.actionConvertTranspose)
        self.menuMove.addAction(self.actionMoveLineUp)
        self.menuMove.addAction(self.actionMoveLineDown)
        self.menuMove.addAction(self.actionMoveColumnLeft)
        self.menuMove.addAction(self.actionMoveColumnRight)
        self.menuText.addAction(self.menuConvert.menuAction())
        self.menuText.addAction(self.menuMove.menuAction())
        self.menuText.addSeparator()
        self.menuText.addAction(self.actionExecute)
        self.menuText.addAction(self.actionFilterThroughCommand)
        self.menuNavigation.addAction(self.actionToggleBookmark)
        self.menuNavigation.addAction(self.actionNextBookmark)
        self.menuNavigation.addAction(self.actionPreviousBookmark)
        self.menuNavigation.addAction(self.actionRemoveAllBookmarks)
        self.menuNavigation.addSeparator()
        self.menuNavigation.addAction(self.actionNextTab)
        self.menuNavigation.addAction(self.actionPreviousTab)
        self.menuNavigation.addAction(self.actionGoToSymbol)
        self.menuNavigation.addAction(self.actionGoToTab)
        self.menuNavigation.addSeparator()
        self.menuNavigation.addAction(self.actionGoToLine)
        self.menuNavigation.addSeparator()
        self.menuNavigation.addAction(self.actionChooseTab)
        self.menuHelp.addAction(self.actionReport_Bug)
        self.menuHelp.addAction(self.actionTranslate_this_application)
        self.menuHelp.addAction(self.actionProjectHomepage)
        self.menuHelp.addAction(self.actionRead_documentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionTakeScreenshot)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuHelp.addAction(self.actionAbout_this_application)
        self.menuSelect.addAction(self.actionSelectWord)
        self.menuSelect.addAction(self.actionSelectLine)
        self.menuSelect.addAction(self.actionSelectParagraph)
        self.menuSelect.addAction(self.actionSelectEnclosingBrackets)
        self.menuSelect.addAction(self.actionSelectCurrentScope)
        self.menuSelect.addAction(self.actionSelectAll)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuSelect.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFindReplace)
        self.menuBundleEditor.addAction(self.actionShowBundleEditor)
        self.menuBundleEditor.addSeparator()
        self.menuBundleEditor.addAction(self.actionEditCommands)
        self.menuBundleEditor.addAction(self.actionEditLanguages)
        self.menuBundleEditor.addAction(self.actionEditSnippets)
        self.menuBundleEditor.addSeparator()
        self.menuBundleEditor.addAction(self.actionReloadBundles)
        self.menuBundles.addAction(self.actionSelectBundleItem)
        self.menuBundles.addSeparator()
        self.menuBundles.addAction(self.menuBundleEditor.menuAction())
        self.menuBundles.addSeparator()
        self.menuPreferences.addAction(self.actionShowMenus)
        self.menuPreferences.addAction(self.actionShowStatus)
        self.menuPreferences.addAction(self.actionFullscreen)
        self.menuPreferences.addSeparator()
        self.menuPreferences.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuText.menuAction())
        self.menubar.addAction(self.menuNavigation.menuAction())
        self.menubar.addAction(self.menuBundles.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_('Prymatex Text Editor'))
        self.menuFile.setTitle(_('&File'))
        self.menuRecentFiles.setTitle(_('Recent Files'))
        self.menuView.setTitle(_('&View'))
        self.menuGutter.setTitle(_('Gutter'))
        self.menuFont.setTitle(_('Font'))
        self.menuPanels.setTitle(_('Panels'))
        self.menuText.setTitle(_('&Text'))
        self.menuConvert.setTitle(_('Convert'))
        self.menuMove.setTitle(_('Move'))
        self.menuNavigation.setTitle(_('&Navigation'))
        self.menuHelp.setTitle(_('&Help'))
        self.menuEdit.setTitle(_('&Edit'))
        self.menuSelect.setTitle(_('Select'))
        self.menuBundles.setTitle(_('&Bundles'))
        self.menuBundleEditor.setTitle(_('Bundle &Editor'))
        self.menuPreferences.setTitle(_('Preferences'))
        self.actionNew.setText(_('&New'))
        self.actionNew.setShortcut(_('Ctrl+N'))
        self.actionOpen.setText(_('Open'))
        self.actionOpen.setShortcut(_('Ctrl+O'))
        self.actionSave.setText(_('Save'))
        self.actionSave.setShortcut(_('Ctrl+S'))
        self.actionSaveAs.setText(_('Save As'))
        self.actionSaveAs.setShortcut(_('Ctrl+Shift+S'))
        self.actionSaveAll.setText(_('Save All'))
        self.actionSaveAll.setShortcut(_('Ctrl+Alt+S'))
        self.actionClose.setText(_('Close'))
        self.actionClose.setShortcut(_('Ctrl+W'))
        self.actionCloseOthers.setText(_('Close Others'))
        self.actionCloseOthers.setShortcut(_('Ctrl+Alt+W'))
        self.actionQuit.setText(_('Quit'))
        self.actionQuit.setShortcut(_('Ctrl+Q'))
        self.actionUndo.setText(_('Undo'))
        self.actionUndo.setShortcut(_('Ctrl+Z'))
        self.actionRedo.setText(_('Redo'))
        self.actionRedo.setShortcut(_('Ctrl+Shift+Z'))
        self.actionCopy.setText(_('Copy'))
        self.actionCopy.setShortcut(_('Ctrl+C'))
        self.actionCut.setText(_('Cut'))
        self.actionCut.setShortcut(_('Ctrl+X'))
        self.actionPaste.setText(_('Paste'))
        self.actionPaste.setShortcut(_('Ctrl+V'))
        self.actionFind.setText(_('Find'))
        self.actionFind.setShortcut(_('Ctrl+F'))
        self.actionSettings.setText(_('Settings'))
        self.actionSettings.setShortcut(_('Alt+P'))
        self.actionFullscreen.setText(_('Fullscreen'))
        self.actionFullscreen.setShortcut(_('F11'))
        self.actionShowMenus.setText(_('Show Menus'))
        self.actionShowMenus.setShortcut(_('Ctrl+M'))
        self.actionZoomIn.setText(_('Zoom In'))
        self.actionZoomIn.setShortcut(_('Ctrl++'))
        self.actionZoomOut.setText(_('Zoom Out'))
        self.actionZoomOut.setShortcut(_('Ctrl+-'))
        self.actionShowLineNumbers.setText(_('Line Numbers'))
        self.actionShowLineNumbers.setShortcut(_('F10'))
        self.actionShowFolding.setText(_('Foldings'))
        self.actionShowFolding.setShortcut(_('Shift+F10'))
        self.actionShowBookmarks.setText(_('Bookmarks'))
        self.actionShowBookmarks.setShortcut(_('Alt+F10'))
        self.actionConvertToUppercase.setText(_('To Uppercase'))
        self.actionConvertToUppercase.setShortcut(_('Ctrl+U'))
        self.actionConvertToLowercase.setText(_('To Lowercase'))
        self.actionConvertToLowercase.setShortcut(_('Ctrl+Shift+U'))
        self.actionConvertToTitlecase.setText(_('To Titlecase'))
        self.actionConvertToTitlecase.setShortcut(_('Ctrl+Alt+U'))
        self.actionConvertToOppositeCase.setText(_('To Opposite Case'))
        self.actionConvertToOppositeCase.setShortcut(_('Ctrl+G'))
        self.actionConvertTranspose.setText(_('Transpose'))
        self.actionConvertTranspose.setShortcut(_('Ctrl+T'))
        self.actionConvertTabToSpaces.setText(_('Tab to Spaces'))
        self.actionConvertSpacesToTabs.setText(_('Spaces to Tabs'))
        self.actionFilterThroughCommand.setText(_('Filter Through Command'))
        self.actionFilterThroughCommand.setIconText(_('Filter Through Command'))
        self.actionExecute.setText(_('Execute Line/Selection'))
        self.actionToggleBookmark.setText(_('&Toggle Bookmark'))
        self.actionToggleBookmark.setShortcut(_('Meta+F12'))
        self.actionNextBookmark.setText(_('&Next Bookmark'))
        self.actionNextBookmark.setShortcut(_('Meta+Alt+F12'))
        self.actionPreviousBookmark.setText(_('&Previous Bookmark'))
        self.actionPreviousBookmark.setShortcut(_('Meta+Shift+F12'))
        self.actionRemoveAllBookmarks.setText(_('&Remove All Bookmarks'))
        self.actionRemoveAllBookmarks.setShortcut(_('Meta+Ctrl+F12'))
        self.actionNextTab.setText(_('N&ext Tab'))
        self.actionNextTab.setShortcut(_('Ctrl+PgDown'))
        self.actionPreviousTab.setText(_('P&revious Tab'))
        self.actionPreviousTab.setShortcut(_('Ctrl+PgUp'))
        self.actionReport_Bug.setText(_('Report &Bug'))
        self.actionTranslate_this_application.setText(_('&Translate this application'))
        self.actionProjectHomepage.setText(_('Project &Homepage'))
        self.actionTakeScreenshot.setText(_('Take &Screenshot'))
        self.actionAbout_this_application.setText(_('&About this application'))
        self.actionAboutQt.setText(_('About &Qt'))
        self.actionNewFromTemplate.setText(_('New From Template'))
        self.actionNewFromTemplate.setShortcut(_('Meta+Shift+N'))
        self.actionShowTabsAndSpaces.setText(_('Show Tabs And Spaces'))
        self.actionShowLineAndParagraphs.setText(_('Show Line And Paragraph'))
        self.actionRead_documentation.setText(_('Read &documentation'))
        self.actionSelectWord.setText(_('&Word'))
        self.actionSelectLine.setText(_('&Line'))
        self.actionSelectParagraph.setText(_('&Paragraph'))
        self.actionSelectEnclosingBrackets.setText(_('Enclosing &Brackets'))
        self.actionSelectCurrentScope.setText(_('Current &Scope'))
        self.actionSelectAll.setText(_('&All'))
        self.actionCloseAll.setText(_('Close All'))
        self.actionShowStatus.setText(_('Show Status'))
        self.actionFindReplace.setText(_('Replace'))
        self.actionOpenAllRecentFiles.setText(_('Open All Recent Files'))
        self.actionRemoveAllRecentFiles.setText(_('Remove All Recent Files'))
        self.actionShowBundleEditor.setText(_('Show Bundle &Editor'))
        self.actionShowBundleEditor.setShortcut(_('Meta+Ctrl+Alt+B'))
        self.actionEditCommands.setText(_('Edit &Commands'))
        self.actionEditCommands.setShortcut(_('Meta+Ctrl+Alt+C'))
        self.actionEditLanguages.setText(_('Edit &Languages'))
        self.actionEditLanguages.setShortcut(_('Meta+Ctrl+Alt+L'))
        self.actionEditSnippets.setText(_('Edit &Snippets'))
        self.actionEditSnippets.setShortcut(_('Meta+Ctrl+Alt+S'))
        self.actionReloadBundles.setText(_('Reload &Bundles'))
        self.actionSelectBundleItem.setText(_('&Select Bundle Item'))
        self.actionSelectBundleItem.setShortcut(_('Meta+Ctrl+T'))
        self.actionGoToLine.setText(_('Go To &Line'))
        self.actionGoToTab.setText(_('Go To Ta&b'))
        self.actionGoToSymbol.setText(_('&Go To Symbol'))
        self.actionChooseTab.setText(_('&Choose Tab...'))
        self.actionMoveLineUp.setText(_('Line Up'))
        self.actionMoveLineUp.setShortcut(_('Meta+Ctrl+Up'))
        self.actionMoveLineDown.setText(_('Line Down'))
        self.actionMoveLineDown.setShortcut(_('Meta+Ctrl+Down'))
        self.actionMoveColumnRight.setText(_('Column Right'))
        self.actionMoveColumnRight.setShortcut(_('Meta+Ctrl+Right'))
        self.actionMoveColumnLeft.setText(_('Column Left'))
        self.actionMoveColumnLeft.setShortcut(_('Meta+Ctrl+Left'))

from prymatex.gui.central.splitter import PMXSplitTabWidget
from prymatex import resources_rc
