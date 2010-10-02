# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/mainwindow.ui'
#
# Created: Tue Jul 13 12:01:56 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icons/Prymatex_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.tabWidgetEditors = PMXTabWidget(MainWindow)
        self.tabWidgetEditors.setObjectName("tabWidgetEditors")
        self.verticalLayout = QtGui.QVBoxLayout(self.tabWidgetEditors)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuText = QtGui.QMenu(self.menubar)
        self.menuText.setObjectName("menuText")
        self.menuConvert = QtGui.QMenu(self.menuText)
        self.menuConvert.setObjectName("menuConvert")
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuRun = QtGui.QMenu(self.menuTools)
        self.menuRun.setObjectName("menuRun")
        self.menuNavigation = QtGui.QMenu(self.menubar)
        self.menuNavigation.setObjectName("menuNavigation")
        self.menuPanes = QtGui.QMenu(self.menuNavigation)
        self.menuPanes.setObjectName("menuPanes")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuBundles = QtGui.QMenu(self.menubar)
        self.menuBundles.setObjectName("menuBundles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = PMXStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewTab = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/actions/document-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewTab.setIcon(icon1)
        self.actionNewTab.setObjectName("actionNewTab")
        self.actionOpen = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resources/actions/document-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resources/actions/document-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/resources/actions/document-save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon4)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_All = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/resources/actions/document-save-all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_All.setIcon(icon5)
        self.actionSave_All.setObjectName("actionSave_All")
        self.actionReload = QtGui.QAction(MainWindow)
        self.actionReload.setObjectName("actionReload")
        self.actionClose = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/resources/actions/tab-close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon6)
        self.actionClose.setObjectName("actionClose")
        self.actionClose_Others = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/resources/actions/tab-close-other.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose_Others.setIcon(icon7)
        self.actionClose_Others.setObjectName("actionClose_Others")
        self.actionRestart = QtGui.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.actionQuit = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/resources/actions/system-shutdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon8)
        self.actionQuit.setObjectName("actionQuit")
        self.actionUndo = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/resources/actions/edit-undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon9)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/resources/actions/edit-redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon10)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCopy = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/resources/actions/edit-copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon11)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/resources/actions/edit-cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon12)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/resources/actions/edit-paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon13)
        self.actionPaste.setObjectName("actionPaste")
        self.actionPaste_As_New = QtGui.QAction(MainWindow)
        self.actionPaste_As_New.setIcon(icon13)
        self.actionPaste_As_New.setObjectName("actionPaste_As_New")
        self.actionFind = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/resources/actions/edit-find-project.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon14)
        self.actionFind.setObjectName("actionFind")
        self.actionFind_Replace = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/resources/actions/edit-find-replace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind_Replace.setIcon(icon15)
        self.actionFind_Replace.setObjectName("actionFind_Replace")
        self.actionPreferences = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/resources/actions/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon16)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionFullscreen = QtGui.QAction(MainWindow)
        self.actionFullscreen.setCheckable(True)
        self.actionFullscreen.setObjectName("actionFullscreen")
        self.actionShow_Menus = QtGui.QAction(MainWindow)
        self.actionShow_Menus.setCheckable(True)
        self.actionShow_Menus.setChecked(True)
        self.actionShow_Menus.setObjectName("actionShow_Menus")
        self.actionZoom_In = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/resources/actions/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_In.setIcon(icon17)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/resources/actions/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_Out.setIcon(icon18)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionFocus_Editor = QtGui.QAction(MainWindow)
        self.actionFocus_Editor.setObjectName("actionFocus_Editor")
        self.actionShow_Line_Numbers = QtGui.QAction(MainWindow)
        self.actionShow_Line_Numbers.setObjectName("actionShow_Line_Numbers")
        self.actionShow_Folding = QtGui.QAction(MainWindow)
        self.actionShow_Folding.setObjectName("actionShow_Folding")
        self.actionShow_Bookmarks_Fold = QtGui.QAction(MainWindow)
        self.actionShow_Bookmarks_Fold.setObjectName("actionShow_Bookmarks_Fold")
        self.actionShow_File_System_Pane = QtGui.QAction(MainWindow)
        self.actionShow_File_System_Pane.setCheckable(True)
        self.actionShow_File_System_Pane.setObjectName("actionShow_File_System_Pane")
        self.actionShow_Project_Dock = QtGui.QAction(MainWindow)
        self.actionShow_Project_Dock.setCheckable(True)
        self.actionShow_Project_Dock.setObjectName("actionShow_Project_Dock")
        self.actionShow_Symbol_List = QtGui.QAction(MainWindow)
        self.actionShow_Symbol_List.setCheckable(True)
        self.actionShow_Symbol_List.setObjectName("actionShow_Symbol_List")
        self.actionShow_Output = QtGui.QAction(MainWindow)
        self.actionShow_Output.setCheckable(True)
        self.actionShow_Output.setObjectName("actionShow_Output")
        self.actionShow_Current_Scope = QtGui.QAction(MainWindow)
        self.actionShow_Current_Scope.setObjectName("actionShow_Current_Scope")
        self.actionShilft_Left = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/resources/actions/format-indent-less.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShilft_Left.setIcon(icon19)
        self.actionShilft_Left.setObjectName("actionShilft_Left")
        self.actionShift_Right = QtGui.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/resources/actions/format-indent-more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShift_Right.setIcon(icon20)
        self.actionShift_Right.setObjectName("actionShift_Right")
        self.actionTo_UPPERCASE = QtGui.QAction(MainWindow)
        self.actionTo_UPPERCASE.setObjectName("actionTo_UPPERCASE")
        self.actionTo_lowercase = QtGui.QAction(MainWindow)
        self.actionTo_lowercase.setObjectName("actionTo_lowercase")
        self.actionTo_TitleCase = QtGui.QAction(MainWindow)
        self.actionTo_TitleCase.setObjectName("actionTo_TitleCase")
        self.actionTo_iNVERT_cASE = QtGui.QAction(MainWindow)
        self.actionTo_iNVERT_cASE.setObjectName("actionTo_iNVERT_cASE")
        self.actionTranspose = QtGui.QAction(MainWindow)
        self.actionTranspose.setObjectName("actionTranspose")
        self.actionTab_to_spaces = QtGui.QAction(MainWindow)
        self.actionTab_to_spaces.setObjectName("actionTab_to_spaces")
        self.actionSpaces_to_Tabs = QtGui.QAction(MainWindow)
        self.actionSpaces_to_Tabs.setObjectName("actionSpaces_to_Tabs")
        self.actionFilter_Through_Command = QtGui.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/resources/actions/view-filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFilter_Through_Command.setIcon(icon21)
        self.actionFilter_Through_Command.setObjectName("actionFilter_Through_Command")
        self.actionRun_selection = QtGui.QAction(MainWindow)
        self.actionRun_selection.setObjectName("actionRun_selection")
        self.actionTermial = QtGui.QAction(MainWindow)
        self.actionTermial.setObjectName("actionTermial")
        self.actionFile_browser = QtGui.QAction(MainWindow)
        self.actionFile_browser.setObjectName("actionFile_browser")
        self.actionThis_file = QtGui.QAction(MainWindow)
        self.actionThis_file.setObjectName("actionThis_file")
        self.actionWith_options = QtGui.QAction(MainWindow)
        self.actionWith_options.setObjectName("actionWith_options")
        self.actionToggle_Bookmark = QtGui.QAction(MainWindow)
        self.actionToggle_Bookmark.setObjectName("actionToggle_Bookmark")
        self.actionNext_Bookmark = QtGui.QAction(MainWindow)
        self.actionNext_Bookmark.setObjectName("actionNext_Bookmark")
        self.actionPrevious_Bookmark = QtGui.QAction(MainWindow)
        self.actionPrevious_Bookmark.setObjectName("actionPrevious_Bookmark")
        self.actionRemove_All_Bookmarks = QtGui.QAction(MainWindow)
        self.actionRemove_All_Bookmarks.setObjectName("actionRemove_All_Bookmarks")
        self.actionNext_Tab = QtGui.QAction(MainWindow)
        self.actionNext_Tab.setObjectName("actionNext_Tab")
        self.actionPrevious_Tab = QtGui.QAction(MainWindow)
        self.actionPrevious_Tab.setObjectName("actionPrevious_Tab")
        self.actionMove_Tab_Left = QtGui.QAction(MainWindow)
        self.actionMove_Tab_Left.setObjectName("actionMove_Tab_Left")
        self.actionMove_Tab_Right = QtGui.QAction(MainWindow)
        self.actionMove_Tab_Right.setObjectName("actionMove_Tab_Right")
        self.actionA = QtGui.QAction(MainWindow)
        self.actionA.setObjectName("actionA")
        self.actionGo_To_Header_Source = QtGui.QAction(MainWindow)
        self.actionGo_To_Header_Source.setObjectName("actionGo_To_Header_Source")
        self.actionGo_To_FIle = QtGui.QAction(MainWindow)
        self.actionGo_To_FIle.setObjectName("actionGo_To_FIle")
        self.actionGo_To_Symbol = QtGui.QAction(MainWindow)
        self.actionGo_To_Symbol.setObjectName("actionGo_To_Symbol")
        self.actionGo_To_Matching_Bracket = QtGui.QAction(MainWindow)
        self.actionGo_To_Matching_Bracket.setObjectName("actionGo_To_Matching_Bracket")
        self.actionGo_To_Line = QtGui.QAction(MainWindow)
        self.actionGo_To_Line.setObjectName("actionGo_To_Line")
        self.actionReport_Bug = QtGui.QAction(MainWindow)
        self.actionReport_Bug.setObjectName("actionReport_Bug")
        self.actionTranslate_this_application = QtGui.QAction(MainWindow)
        self.actionTranslate_this_application.setObjectName("actionTranslate_this_application")
        self.actionProject_Homepage = QtGui.QAction(MainWindow)
        self.actionProject_Homepage.setObjectName("actionProject_Homepage")
        self.actionTake_Screenshot = QtGui.QAction(MainWindow)
        self.actionTake_Screenshot.setObjectName("actionTake_Screenshot")
        self.actionAbout_this_application = QtGui.QAction(MainWindow)
        self.actionAbout_this_application.setObjectName("actionAbout_this_application")
        self.actionAbout_Qt = QtGui.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionShow_Bundle_Editor = QtGui.QAction(MainWindow)
        self.actionShow_Bundle_Editor.setCheckable(True)
        self.actionShow_Bundle_Editor.setObjectName("actionShow_Bundle_Editor")
        self.actionSelect_Bundle_Item = QtGui.QAction(MainWindow)
        self.actionSelect_Bundle_Item.setObjectName("actionSelect_Bundle_Item")
        self.actionSelect_All = QtGui.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionSelect_None = QtGui.QAction(MainWindow)
        self.actionSelect_None.setObjectName("actionSelect_None")
        self.menuFile.addAction(self.actionNewTab)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionSave_All)
        self.menuFile.addAction(self.actionReload)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionClose_Others)
        self.menuFile.addAction(self.actionRestart)
        self.menuFile.addAction(self.actionQuit)
        self.menuView.addAction(self.actionFullscreen)
        self.menuView.addAction(self.actionShow_Menus)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionFocus_Editor)
        self.menuView.addAction(self.actionShow_Line_Numbers)
        self.menuView.addAction(self.actionShow_Folding)
        self.menuView.addAction(self.actionShow_Bookmarks_Fold)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionShow_File_System_Pane)
        self.menuView.addAction(self.actionShow_Project_Dock)
        self.menuView.addAction(self.actionShow_Symbol_List)
        self.menuView.addAction(self.actionShow_Output)
        self.menuView.addSeparator()
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionShow_Current_Scope)
        self.menuConvert.addAction(self.actionTo_UPPERCASE)
        self.menuConvert.addAction(self.actionTo_lowercase)
        self.menuConvert.addAction(self.actionTo_TitleCase)
        self.menuConvert.addAction(self.actionTo_iNVERT_cASE)
        self.menuConvert.addAction(self.actionTranspose)
        self.menuText.addAction(self.menuConvert.menuAction())
        self.menuText.addAction(self.actionShilft_Left)
        self.menuText.addAction(self.actionShift_Right)
        self.menuText.addSeparator()
        self.menuText.addAction(self.actionTab_to_spaces)
        self.menuText.addAction(self.actionSpaces_to_Tabs)
        self.menuText.addSeparator()
        self.menuText.addAction(self.actionFilter_Through_Command)
        self.menuText.addAction(self.actionRun_selection)
        self.menuRun.addAction(self.actionThis_file)
        self.menuRun.addAction(self.actionWith_options)
        self.menuTools.addAction(self.menuRun.menuAction())
        self.menuTools.addAction(self.actionTermial)
        self.menuTools.addAction(self.actionFile_browser)
        self.menuNavigation.addAction(self.actionToggle_Bookmark)
        self.menuNavigation.addAction(self.actionNext_Bookmark)
        self.menuNavigation.addAction(self.actionPrevious_Bookmark)
        self.menuNavigation.addAction(self.actionRemove_All_Bookmarks)
        self.menuNavigation.addSeparator()
        self.menuNavigation.addAction(self.actionNext_Tab)
        self.menuNavigation.addAction(self.actionPrevious_Tab)
        self.menuNavigation.addAction(self.actionMove_Tab_Left)
        self.menuNavigation.addAction(self.actionMove_Tab_Right)
        self.menuNavigation.addAction(self.menuPanes.menuAction())
        self.menuNavigation.addSeparator()
        self.menuNavigation.addAction(self.actionGo_To_Header_Source)
        self.menuNavigation.addAction(self.actionGo_To_FIle)
        self.menuNavigation.addAction(self.actionGo_To_Symbol)
        self.menuNavigation.addAction(self.actionGo_To_Matching_Bracket)
        self.menuNavigation.addAction(self.actionGo_To_Line)
        self.menuHelp.addAction(self.actionReport_Bug)
        self.menuHelp.addAction(self.actionTranslate_this_application)
        self.menuHelp.addAction(self.actionProject_Homepage)
        self.menuHelp.addAction(self.actionTake_Screenshot)
        self.menuHelp.addAction(self.actionAbout_this_application)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionPaste_As_New)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFind_Replace)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuEdit.addAction(self.actionSelect_None)
        self.menuBundles.addAction(self.actionShow_Bundle_Editor)
        self.menuBundles.addAction(self.actionSelect_Bundle_Item)
        self.menuBundles.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuText.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuNavigation.menuAction())
        self.menubar.addAction(self.menuBundles.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Prymatex Text Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuText.setTitle(QtGui.QApplication.translate("MainWindow", "&Text", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConvert.setTitle(QtGui.QApplication.translate("MainWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "T&ools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRun.setTitle(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.menuNavigation.setTitle(QtGui.QApplication.translate("MainWindow", "&Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPanes.setTitle(QtGui.QApplication.translate("MainWindow", "Panes", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBundles.setTitle(QtGui.QApplication.translate("MainWindow", "&Bundles", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewTab.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewTab.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_All.setText(QtGui.QApplication.translate("MainWindow", "Save All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_All.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Alt+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReload.setText(QtGui.QApplication.translate("MainWindow", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReload.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_Others.setText(QtGui.QApplication.translate("MainWindow", "Close Others", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_Others.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Alt+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRestart.setText(QtGui.QApplication.translate("MainWindow", "Restart", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRestart.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+Shift+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setText(QtGui.QApplication.translate("MainWindow", "Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUndo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setText(QtGui.QApplication.translate("MainWindow", "Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRedo.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+Z", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste_As_New.setText(QtGui.QApplication.translate("MainWindow", "Paste As New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste_As_New.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setText(QtGui.QApplication.translate("MainWindow", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Replace.setText(QtGui.QApplication.translate("MainWindow", "Find/Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind_Replace.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFullscreen.setText(QtGui.QApplication.translate("MainWindow", "Fullscreen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFullscreen.setShortcut(QtGui.QApplication.translate("MainWindow", "F11", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Menus.setText(QtGui.QApplication.translate("MainWindow", "Show Menus", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Menus.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+M", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_In.setText(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_In.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_Out.setText(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoom_Out.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFocus_Editor.setText(QtGui.QApplication.translate("MainWindow", "Focus Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFocus_Editor.setShortcut(QtGui.QApplication.translate("MainWindow", "F12", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Line_Numbers.setText(QtGui.QApplication.translate("MainWindow", "Show Line Numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Line_Numbers.setShortcut(QtGui.QApplication.translate("MainWindow", "F10", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Folding.setText(QtGui.QApplication.translate("MainWindow", "Show Code Folding", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Folding.setShortcut(QtGui.QApplication.translate("MainWindow", "Shift+F10", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Bookmarks_Fold.setText(QtGui.QApplication.translate("MainWindow", "Show Bookmarks Fold", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Bookmarks_Fold.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+F10", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_File_System_Pane.setText(QtGui.QApplication.translate("MainWindow", "Show File System Navigator", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_File_System_Pane.setShortcut(QtGui.QApplication.translate("MainWindow", "F8", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Project_Dock.setText(QtGui.QApplication.translate("MainWindow", "Show Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Project_Dock.setShortcut(QtGui.QApplication.translate("MainWindow", "F7", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Symbol_List.setText(QtGui.QApplication.translate("MainWindow", "Show Symbol List", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Symbol_List.setShortcut(QtGui.QApplication.translate("MainWindow", "F6", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Output.setText(QtGui.QApplication.translate("MainWindow", "Show Output", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Output.setShortcut(QtGui.QApplication.translate("MainWindow", "Shift+F6", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Current_Scope.setText(QtGui.QApplication.translate("MainWindow", "Show Current Scope", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Current_Scope.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShilft_Left.setText(QtGui.QApplication.translate("MainWindow", "Shilft Left", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShilft_Left.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+<", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShift_Right.setText(QtGui.QApplication.translate("MainWindow", "Shift Right", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShift_Right.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+>", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTo_UPPERCASE.setText(QtGui.QApplication.translate("MainWindow", "To UPPERCASE", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTo_lowercase.setText(QtGui.QApplication.translate("MainWindow", "To lowercase", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTo_TitleCase.setText(QtGui.QApplication.translate("MainWindow", "To TitleCase", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTo_iNVERT_cASE.setText(QtGui.QApplication.translate("MainWindow", "To iNVERT cASE", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTranspose.setText(QtGui.QApplication.translate("MainWindow", "Transpose", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTab_to_spaces.setText(QtGui.QApplication.translate("MainWindow", "Tab to Spaces", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSpaces_to_Tabs.setText(QtGui.QApplication.translate("MainWindow", "Spaces to Tabs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilter_Through_Command.setText(QtGui.QApplication.translate("MainWindow", "Filter through command", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilter_Through_Command.setIconText(QtGui.QApplication.translate("MainWindow", "Filter Through Command", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFilter_Through_Command.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_selection.setText(QtGui.QApplication.translate("MainWindow", "Run selection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_selection.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+Shift+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTermial.setText(QtGui.QApplication.translate("MainWindow", "Termial", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFile_browser.setText(QtGui.QApplication.translate("MainWindow", "File browser", None, QtGui.QApplication.UnicodeUTF8))
        self.actionThis_file.setText(QtGui.QApplication.translate("MainWindow", "This file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWith_options.setText(QtGui.QApplication.translate("MainWindow", "with options...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToggle_Bookmark.setText(QtGui.QApplication.translate("MainWindow", "Toggle Bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToggle_Bookmark.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+B", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext_Bookmark.setText(QtGui.QApplication.translate("MainWindow", "Next Bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext_Bookmark.setShortcut(QtGui.QApplication.translate("MainWindow", "F2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrevious_Bookmark.setText(QtGui.QApplication.translate("MainWindow", "Previous Bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrevious_Bookmark.setShortcut(QtGui.QApplication.translate("MainWindow", "Shift+F3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_All_Bookmarks.setText(QtGui.QApplication.translate("MainWindow", "Remove All Bookmarks", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_All_Bookmarks.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+F3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext_Tab.setText(QtGui.QApplication.translate("MainWindow", "Next Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext_Tab.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+PgDown", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrevious_Tab.setText(QtGui.QApplication.translate("MainWindow", "Previous Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrevious_Tab.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+PgUp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove_Tab_Left.setText(QtGui.QApplication.translate("MainWindow", "Move Tab Left", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove_Tab_Left.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+PgUp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove_Tab_Right.setText(QtGui.QApplication.translate("MainWindow", "Move Tab Right", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMove_Tab_Right.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+PgDown", None, QtGui.QApplication.UnicodeUTF8))
        self.actionA.setText(QtGui.QApplication.translate("MainWindow", "No Pane", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGo_To_Header_Source.setText(QtGui.QApplication.translate("MainWindow", "Go To Header/Source", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGo_To_FIle.setText(QtGui.QApplication.translate("MainWindow", "Go To FIle", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGo_To_Symbol.setText(QtGui.QApplication.translate("MainWindow", "Go To Symbol", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGo_To_Matching_Bracket.setText(QtGui.QApplication.translate("MainWindow", "Go To Matching Bracket", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGo_To_Matching_Bracket.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+B", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGo_To_Line.setText(QtGui.QApplication.translate("MainWindow", "Go To Line", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGo_To_Line.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+G", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReport_Bug.setText(QtGui.QApplication.translate("MainWindow", "Report Bug", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTranslate_this_application.setText(QtGui.QApplication.translate("MainWindow", "Translate this application", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProject_Homepage.setText(QtGui.QApplication.translate("MainWindow", "Project Homepage", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTake_Screenshot.setText(QtGui.QApplication.translate("MainWindow", "Take Screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_this_application.setText(QtGui.QApplication.translate("MainWindow", "About this application", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Qt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShow_Bundle_Editor.setText(QtGui.QApplication.translate("MainWindow", "Show Bundle Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_Bundle_Item.setText(QtGui.QApplication.translate("MainWindow", "Select Bundle Item", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_Bundle_Item.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Alt+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_All.setText(QtGui.QApplication.translate("MainWindow", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_None.setText(QtGui.QApplication.translate("MainWindow", "Select None", None, QtGui.QApplication.UnicodeUTF8))

from statusbar import PMXStatusBar
from tabwidget import PMXTabWidget
import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
