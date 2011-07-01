# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/editorwidget.ui'
#
# Created: Fri Apr 22 20:33:44 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EditorWidget(object):
    def setupUi(self, EditorWidget):
        EditorWidget.setObjectName(_fromUtf8("EditorWidget"))
        EditorWidget.resize(788, 482)
        self.verticalLayout = QtGui.QVBoxLayout(EditorWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.codeEdit = PMXCodeEdit(EditorWidget)
        self.codeEdit.setObjectName(_fromUtf8("codeEdit"))
        self.verticalLayout.addWidget(self.codeEdit)
        self.goToLineWidget = PMXRefocusWidget(EditorWidget)
        self.goToLineWidget.setObjectName(_fromUtf8("goToLineWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.goToLineWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelGoToLine = QtGui.QLabel(self.goToLineWidget)
        self.labelGoToLine.setObjectName(_fromUtf8("labelGoToLine"))
        self.horizontalLayout.addWidget(self.labelGoToLine)
        self.spinLineNumbers = PMXSpinGoToLine(self.goToLineWidget)
        self.spinLineNumbers.setMinimum(1)
        self.spinLineNumbers.setObjectName(_fromUtf8("spinLineNumbers"))
        self.horizontalLayout.addWidget(self.spinLineNumbers)
        self.pushGoToLine = QtGui.QPushButton(self.goToLineWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/resources/actions/go-next-view.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushGoToLine.setIcon(icon)
        self.pushGoToLine.setAutoDefault(True)
        self.pushGoToLine.setDefault(True)
        self.pushGoToLine.setObjectName(_fromUtf8("pushGoToLine"))
        self.horizontalLayout.addWidget(self.pushGoToLine)
        spacerItem = QtGui.QSpacerItem(154, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushCloseGoToLine = QtGui.QPushButton(self.goToLineWidget)
        self.pushCloseGoToLine.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/resources/actions/process-stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushCloseGoToLine.setIcon(icon1)
        self.pushCloseGoToLine.setFlat(True)
        self.pushCloseGoToLine.setObjectName(_fromUtf8("pushCloseGoToLine"))
        self.horizontalLayout.addWidget(self.pushCloseGoToLine)
        self.verticalLayout.addWidget(self.goToLineWidget)
        self.findReplaceWidget = PMXFindReplaceWidget(EditorWidget)
        self.findReplaceWidget.setObjectName(_fromUtf8("findReplaceWidget"))
        self.gridLayout = QtGui.QGridLayout(self.findReplaceWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelFind = QtGui.QLabel(self.findReplaceWidget)
        self.labelFind.setObjectName(_fromUtf8("labelFind"))
        self.gridLayout.addWidget(self.labelFind, 0, 0, 1, 1)
        self.pushFindPrevious = QtGui.QPushButton(self.findReplaceWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Mono L"))
        font.setWeight(75)
        font.setBold(True)
        self.pushFindPrevious.setFont(font)
        self.pushFindPrevious.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/resources/actions/go-previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushFindPrevious.setIcon(icon2)
        self.pushFindPrevious.setObjectName(_fromUtf8("pushFindPrevious"))
        self.gridLayout.addWidget(self.pushFindPrevious, 0, 3, 1, 1)
        self.pushFindNext = QtGui.QPushButton(self.findReplaceWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Mono L"))
        font.setWeight(75)
        font.setBold(True)
        self.pushFindNext.setFont(font)
        self.pushFindNext.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/resources/actions/go-next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushFindNext.setIcon(icon3)
        self.pushFindNext.setAutoDefault(True)
        self.pushFindNext.setObjectName(_fromUtf8("pushFindNext"))
        self.gridLayout.addWidget(self.pushFindNext, 0, 4, 1, 1)
        self.pushOptions = QtGui.QPushButton(self.findReplaceWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/resources/actions/configure.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushOptions.setIcon(icon4)
        self.pushOptions.setObjectName(_fromUtf8("pushOptions"))
        self.gridLayout.addWidget(self.pushOptions, 0, 5, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 7, 1, 1)
        self.pushCloseFindreplace = QtGui.QPushButton(self.findReplaceWidget)
        self.pushCloseFindreplace.setText(_fromUtf8(""))
        self.pushCloseFindreplace.setIcon(icon1)
        self.pushCloseFindreplace.setFlat(True)
        self.pushCloseFindreplace.setObjectName(_fromUtf8("pushCloseFindreplace"))
        self.gridLayout.addWidget(self.pushCloseFindreplace, 0, 8, 1, 1)
        self.labelReplaceWith = QtGui.QLabel(self.findReplaceWidget)
        self.labelReplaceWith.setObjectName(_fromUtf8("labelReplaceWith"))
        self.gridLayout.addWidget(self.labelReplaceWith, 1, 0, 1, 1)
        self.pushReplaceAndFindPrevious = QtGui.QPushButton(self.findReplaceWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Mono L"))
        font.setWeight(75)
        font.setBold(True)
        self.pushReplaceAndFindPrevious.setFont(font)
        self.pushReplaceAndFindPrevious.setText(_fromUtf8(""))
        self.pushReplaceAndFindPrevious.setIcon(icon2)
        self.pushReplaceAndFindPrevious.setObjectName(_fromUtf8("pushReplaceAndFindPrevious"))
        self.gridLayout.addWidget(self.pushReplaceAndFindPrevious, 1, 3, 1, 1)
        self.pushReplaceAndFindNext = QtGui.QPushButton(self.findReplaceWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Mono L"))
        font.setWeight(75)
        font.setBold(True)
        self.pushReplaceAndFindNext.setFont(font)
        self.pushReplaceAndFindNext.setText(_fromUtf8(""))
        self.pushReplaceAndFindNext.setIcon(icon3)
        self.pushReplaceAndFindNext.setObjectName(_fromUtf8("pushReplaceAndFindNext"))
        self.gridLayout.addWidget(self.pushReplaceAndFindNext, 1, 4, 1, 1)
        self.pushReplaceAll = QtGui.QPushButton(self.findReplaceWidget)
        self.pushReplaceAll.setFlat(True)
        self.pushReplaceAll.setObjectName(_fromUtf8("pushReplaceAll"))
        self.gridLayout.addWidget(self.pushReplaceAll, 1, 5, 1, 1)
        self.comboFind = PMXFindBox(self.findReplaceWidget)
        self.comboFind.setMinimumSize(QtCore.QSize(300, 0))
        self.comboFind.setEditable(True)
        self.comboFind.setObjectName(_fromUtf8("comboFind"))
        self.gridLayout.addWidget(self.comboFind, 0, 2, 1, 1)
        self.comboReplace = PMXReplaceBox(self.findReplaceWidget)
        self.comboReplace.setEditable(True)
        self.comboReplace.setObjectName(_fromUtf8("comboReplace"))
        self.gridLayout.addWidget(self.comboReplace, 1, 2, 1, 1)
        self.labelMatchCounter = QtGui.QLabel(self.findReplaceWidget)
        self.labelMatchCounter.setObjectName(_fromUtf8("labelMatchCounter"))
        self.gridLayout.addWidget(self.labelMatchCounter, 0, 6, 1, 1)
        self.verticalLayout.addWidget(self.findReplaceWidget)

        self.retranslateUi(EditorWidget)
        QtCore.QObject.connect(self.pushCloseGoToLine, QtCore.SIGNAL(_fromUtf8("pressed()")), self.goToLineWidget.hide)
        QtCore.QMetaObject.connectSlotsByName(EditorWidget)

    def retranslateUi(self, EditorWidget):
        EditorWidget.setWindowTitle(QtGui.QApplication.translate("EditorWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.labelGoToLine.setText(QtGui.QApplication.translate("EditorWidget", "Go to line:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushGoToLine.setText(QtGui.QApplication.translate("EditorWidget", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFind.setText(QtGui.QApplication.translate("EditorWidget", "Find:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushFindPrevious.setToolTip(QtGui.QApplication.translate("EditorWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nimbus Mono L\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Find Previous</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushFindNext.setToolTip(QtGui.QApplication.translate("EditorWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nimbus Mono L\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Find Next</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushOptions.setText(QtGui.QApplication.translate("EditorWidget", "Opt&ions", None, QtGui.QApplication.UnicodeUTF8))
        self.labelReplaceWith.setText(QtGui.QApplication.translate("EditorWidget", "Replace with:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushReplaceAndFindPrevious.setToolTip(QtGui.QApplication.translate("EditorWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nimbus Mono L\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Replace &amp; Find Previous</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushReplaceAll.setText(QtGui.QApplication.translate("EditorWidget", "Replace &All", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMatchCounter.setText(QtGui.QApplication.translate("EditorWidget", "0 matches", None, QtGui.QApplication.UnicodeUTF8))

from codeedit import PMXCodeEdit
from findreplace import PMXFindBox, PMXFindReplaceWidget, PMXReplaceBox
from internalwidgets import PMXRefocusWidget, PMXSpinGoToLine
import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EditorWidget = QtGui.QWidget()
    ui = Ui_EditorWidget()
    ui.setupUi(EditorWidget)
    EditorWidget.show()
    sys.exit(app.exec_())
