# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/font_and_theme.ui'
#
# Created: Thu Mar 31 09:45:10 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_FontThemeConfig(object):
    def setupUi(self, FontThemeConfig):
        FontThemeConfig.setObjectName("FontThemeConfig")
        FontThemeConfig.resize(518, 467)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/actions/resources/actions/format-font-size-more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FontThemeConfig.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(FontThemeConfig)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(FontThemeConfig)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(FontThemeConfig)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(FontThemeConfig)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox = QtGui.QGroupBox(FontThemeConfig)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboThemes = QtGui.QComboBox(self.groupBox)
        self.comboThemes.setObjectName("comboThemes")
        self.horizontalLayout_2.addWidget(self.comboThemes)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.pushForeground = QtGui.QPushButton(self.groupBox)
        self.pushForeground.setText("")
        self.pushForeground.setObjectName("pushForeground")
        self.gridLayout.addWidget(self.pushForeground, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.pushInvisibles = QtGui.QPushButton(self.groupBox)
        self.pushInvisibles.setText("")
        self.pushInvisibles.setObjectName("pushInvisibles")
        self.gridLayout.addWidget(self.pushInvisibles, 0, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.pushBackground = QtGui.QPushButton(self.groupBox)
        self.pushBackground.setText("")
        self.pushBackground.setObjectName("pushBackground")
        self.gridLayout.addWidget(self.pushBackground, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.pushLineHighlight = QtGui.QPushButton(self.groupBox)
        self.pushLineHighlight.setText("")
        self.pushLineHighlight.setObjectName("pushLineHighlight")
        self.gridLayout.addWidget(self.pushLineHighlight, 1, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.pushSelection = QtGui.QPushButton(self.groupBox)
        self.pushSelection.setText("")
        self.pushSelection.setObjectName("pushSelection")
        self.gridLayout.addWidget(self.pushSelection, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)
        self.pushCaret = QtGui.QPushButton(self.groupBox)
        self.pushCaret.setText("")
        self.pushCaret.setObjectName("pushCaret")
        self.gridLayout.addWidget(self.pushCaret, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tableView = QtGui.QTableView(self.groupBox)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_8 = QtGui.QPushButton(self.groupBox)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtGui.QPushButton(self.groupBox)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.comboBox_2 = QtGui.QComboBox(self.groupBox)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(FontThemeConfig)
        QtCore.QMetaObject.connectSlotsByName(FontThemeConfig)

    def retranslateUi(self, FontThemeConfig):
        FontThemeConfig.setWindowTitle(QtGui.QApplication.translate("FontThemeConfig", "Font and Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FontThemeConfig", "Font", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("FontThemeConfig", "Change Font", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FontThemeConfig", "Themes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FontThemeConfig", "Current theme", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FontThemeConfig", "Foreground", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("FontThemeConfig", "Invisibles", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FontThemeConfig", "Background", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("FontThemeConfig", "Line Highlight", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FontThemeConfig", "Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("FontThemeConfig", "Caret", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("FontThemeConfig", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("FontThemeConfig", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("FontThemeConfig", "Scope Selector", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("FontThemeConfig", "Antialias", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FontThemeConfig = QtGui.QWidget()
    ui = Ui_FontThemeConfig()
    ui.setupUi(FontThemeConfig)
    FontThemeConfig.show()
    sys.exit(app.exec_())

