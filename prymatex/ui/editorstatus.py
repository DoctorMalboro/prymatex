# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/editorstatus.ui'
#
# Created: Sat Oct 22 19:27:19 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from prymatex.utils.i18n import ugettext as _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CodeEditorStatus(object):
    def setupUi(self, CodeEditorStatus):
        CodeEditorStatus.setObjectName(_fromUtf8("CodeEditorStatus"))
        CodeEditorStatus.resize(721, 254)
        self.verticalLayout = QtGui.QVBoxLayout(CodeEditorStatus)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widgetCommand = QtGui.QWidget(CodeEditorStatus)
        self.widgetCommand.setObjectName(_fromUtf8("widgetCommand"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widgetCommand)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonCommandClose = QtGui.QPushButton(self.widgetCommand)
        self.pushButtonCommandClose.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/dialog-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCommandClose.setIcon(icon)
        self.pushButtonCommandClose.setFlat(True)
        self.pushButtonCommandClose.setObjectName(_fromUtf8("pushButtonCommandClose"))
        self.horizontalLayout.addWidget(self.pushButtonCommandClose)
        self.label = QtGui.QLabel(self.widgetCommand)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEditCommand = QtGui.QLineEdit(self.widgetCommand)
        self.lineEditCommand.setObjectName(_fromUtf8("lineEditCommand"))
        self.horizontalLayout.addWidget(self.lineEditCommand)
        self.label_2 = QtGui.QLabel(self.widgetCommand)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBoxInput = QtGui.QComboBox(self.widgetCommand)
        self.comboBoxInput.setObjectName(_fromUtf8("comboBoxInput"))
        self.horizontalLayout.addWidget(self.comboBoxInput)
        self.label_3 = QtGui.QLabel(self.widgetCommand)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBoxOutput = QtGui.QComboBox(self.widgetCommand)
        self.comboBoxOutput.setObjectName(_fromUtf8("comboBoxOutput"))
        self.horizontalLayout.addWidget(self.comboBoxOutput)
        self.verticalLayout.addWidget(self.widgetCommand)
        self.widgetGoToLine = QtGui.QWidget(CodeEditorStatus)
        self.widgetGoToLine.setObjectName(_fromUtf8("widgetGoToLine"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widgetGoToLine)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButtonGoToLineClose = QtGui.QPushButton(self.widgetGoToLine)
        self.pushButtonGoToLineClose.setText(_fromUtf8(""))
        self.pushButtonGoToLineClose.setIcon(icon)
        self.pushButtonGoToLineClose.setFlat(True)
        self.pushButtonGoToLineClose.setObjectName(_fromUtf8("pushButtonGoToLineClose"))
        self.horizontalLayout_3.addWidget(self.pushButtonGoToLineClose)
        self.labelGoToLine = QtGui.QLabel(self.widgetGoToLine)
        self.labelGoToLine.setObjectName(_fromUtf8("labelGoToLine"))
        self.horizontalLayout_3.addWidget(self.labelGoToLine)
        self.spinBoxGoToLine = QtGui.QSpinBox(self.widgetGoToLine)
        self.spinBoxGoToLine.setMinimum(1)
        self.spinBoxGoToLine.setMaximum(1000)
        self.spinBoxGoToLine.setObjectName(_fromUtf8("spinBoxGoToLine"))
        self.horizontalLayout_3.addWidget(self.spinBoxGoToLine)
        spacerItem = QtGui.QSpacerItem(154, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widgetGoToLine)
        self.widgetIFind = QtGui.QWidget(CodeEditorStatus)
        self.widgetIFind.setObjectName(_fromUtf8("widgetIFind"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widgetIFind)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButtonIFindClose = QtGui.QPushButton(self.widgetIFind)
        self.pushButtonIFindClose.setText(_fromUtf8(""))
        self.pushButtonIFindClose.setIcon(icon)
        self.pushButtonIFindClose.setFlat(True)
        self.pushButtonIFindClose.setObjectName(_fromUtf8("pushButtonIFindClose"))
        self.horizontalLayout_5.addWidget(self.pushButtonIFindClose)
        self.labelIFind = QtGui.QLabel(self.widgetIFind)
        self.labelIFind.setObjectName(_fromUtf8("labelIFind"))
        self.horizontalLayout_5.addWidget(self.labelIFind)
        self.lineEditIFind = QtGui.QLineEdit(self.widgetIFind)
        self.lineEditIFind.setObjectName(_fromUtf8("lineEditIFind"))
        self.horizontalLayout_5.addWidget(self.lineEditIFind)
        self.pushButtonIFindNext = QtGui.QPushButton(self.widgetIFind)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/go-down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonIFindNext.setIcon(icon1)
        self.pushButtonIFindNext.setObjectName(_fromUtf8("pushButtonIFindNext"))
        self.horizontalLayout_5.addWidget(self.pushButtonIFindNext)
        self.pushButtonIFindPrevious = QtGui.QPushButton(self.widgetIFind)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/go-up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonIFindPrevious.setIcon(icon2)
        self.pushButtonIFindPrevious.setObjectName(_fromUtf8("pushButtonIFindPrevious"))
        self.horizontalLayout_5.addWidget(self.pushButtonIFindPrevious)
        self.checkBoxIFindCaseSensitively = QtGui.QCheckBox(self.widgetIFind)
        self.checkBoxIFindCaseSensitively.setObjectName(_fromUtf8("checkBoxIFindCaseSensitively"))
        self.horizontalLayout_5.addWidget(self.checkBoxIFindCaseSensitively)
        spacerItem1 = QtGui.QSpacerItem(155, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widgetIFind)
        self.widgetFindReplace = QtGui.QWidget(CodeEditorStatus)
        self.widgetFindReplace.setObjectName(_fromUtf8("widgetFindReplace"))
        self.gridLayout = QtGui.QGridLayout(self.widgetFindReplace)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButtonFindReplaceClose = QtGui.QPushButton(self.widgetFindReplace)
        self.pushButtonFindReplaceClose.setText(_fromUtf8(""))
        self.pushButtonFindReplaceClose.setIcon(icon)
        self.pushButtonFindReplaceClose.setFlat(True)
        self.pushButtonFindReplaceClose.setObjectName(_fromUtf8("pushButtonFindReplaceClose"))
        self.gridLayout.addWidget(self.pushButtonFindReplaceClose, 0, 0, 1, 1)
        self.labelFind = QtGui.QLabel(self.widgetFindReplace)
        self.labelFind.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelFind.setObjectName(_fromUtf8("labelFind"))
        self.gridLayout.addWidget(self.labelFind, 0, 1, 1, 1)
        self.labelReplace = QtGui.QLabel(self.widgetFindReplace)
        self.labelReplace.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelReplace.setObjectName(_fromUtf8("labelReplace"))
        self.gridLayout.addWidget(self.labelReplace, 1, 1, 1, 1)
        self.lineEditFind = QtGui.QLineEdit(self.widgetFindReplace)
        self.lineEditFind.setObjectName(_fromUtf8("lineEditFind"))
        self.gridLayout.addWidget(self.lineEditFind, 0, 2, 1, 1)
        self.lineEditReplace = QtGui.QLineEdit(self.widgetFindReplace)
        self.lineEditReplace.setObjectName(_fromUtf8("lineEditReplace"))
        self.gridLayout.addWidget(self.lineEditReplace, 1, 2, 1, 1)
        self.pushButtonReplace = QtGui.QPushButton(self.widgetFindReplace)
        self.pushButtonReplace.setObjectName(_fromUtf8("pushButtonReplace"))
        self.gridLayout.addWidget(self.pushButtonReplace, 1, 4, 1, 1)
        self.pushButtonReplaceAll = QtGui.QPushButton(self.widgetFindReplace)
        self.pushButtonReplaceAll.setObjectName(_fromUtf8("pushButtonReplaceAll"))
        self.gridLayout.addWidget(self.pushButtonReplaceAll, 1, 5, 1, 1)
        self.pushButtonFindPrevious = QtGui.QPushButton(self.widgetFindReplace)
        self.pushButtonFindPrevious.setIcon(icon2)
        self.pushButtonFindPrevious.setObjectName(_fromUtf8("pushButtonFindPrevious"))
        self.gridLayout.addWidget(self.pushButtonFindPrevious, 0, 5, 1, 1)
        self.pushButtonFindNext = QtGui.QPushButton(self.widgetFindReplace)
        self.pushButtonFindNext.setIcon(icon1)
        self.pushButtonFindNext.setObjectName(_fromUtf8("pushButtonFindNext"))
        self.gridLayout.addWidget(self.pushButtonFindNext, 0, 4, 1, 1)
        self.widgetFindReplaceOptions = QtGui.QWidget(self.widgetFindReplace)
        self.widgetFindReplaceOptions.setObjectName(_fromUtf8("widgetFindReplaceOptions"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widgetFindReplaceOptions)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.labelFindMode = QtGui.QLabel(self.widgetFindReplaceOptions)
        self.labelFindMode.setObjectName(_fromUtf8("labelFindMode"))
        self.horizontalLayout_4.addWidget(self.labelFindMode)
        self.comboBoxFindMode = QtGui.QComboBox(self.widgetFindReplaceOptions)
        self.comboBoxFindMode.setObjectName(_fromUtf8("comboBoxFindMode"))
        self.horizontalLayout_4.addWidget(self.comboBoxFindMode)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.checkBoxFindCaseSensitively = QtGui.QCheckBox(self.widgetFindReplaceOptions)
        self.checkBoxFindCaseSensitively.setObjectName(_fromUtf8("checkBoxFindCaseSensitively"))
        self.horizontalLayout_4.addWidget(self.checkBoxFindCaseSensitively)
        self.pushButtonFindAll = QtGui.QPushButton(self.widgetFindReplaceOptions)
        self.pushButtonFindAll.setObjectName(_fromUtf8("pushButtonFindAll"))
        self.horizontalLayout_4.addWidget(self.pushButtonFindAll)
        self.gridLayout.addWidget(self.widgetFindReplaceOptions, 2, 1, 1, 5)
        self.verticalLayout.addWidget(self.widgetFindReplace)
        self.widgetStatus = QtGui.QWidget(CodeEditorStatus)
        self.widgetStatus.setObjectName(_fromUtf8("widgetStatus"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widgetStatus)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelLineColumn = QtGui.QLabel(self.widgetStatus)
        self.labelLineColumn.setObjectName(_fromUtf8("labelLineColumn"))
        self.horizontalLayout_2.addWidget(self.labelLineColumn)
        self.labelTabSize = QtGui.QLabel(self.widgetStatus)
        self.labelTabSize.setMaximumSize(QtCore.QSize(80, 16777215))
        self.labelTabSize.setObjectName(_fromUtf8("labelTabSize"))
        self.horizontalLayout_2.addWidget(self.labelTabSize)
        self.comboBoxSyntaxes = QtGui.QComboBox(self.widgetStatus)
        self.comboBoxSyntaxes.setMaximumSize(QtCore.QSize(160, 16777215))
        self.comboBoxSyntaxes.setObjectName(_fromUtf8("comboBoxSyntaxes"))
        self.horizontalLayout_2.addWidget(self.comboBoxSyntaxes)
        self.comboBoxSymbols = QtGui.QComboBox(self.widgetStatus)
        self.comboBoxSymbols.setMaximumSize(QtCore.QSize(220, 16777215))
        self.comboBoxSymbols.setObjectName(_fromUtf8("comboBoxSymbols"))
        self.horizontalLayout_2.addWidget(self.comboBoxSymbols)
        self.verticalLayout.addWidget(self.widgetStatus)

        self.retranslateUi(CodeEditorStatus)
        QtCore.QMetaObject.connectSlotsByName(CodeEditorStatus)

    def retranslateUi(self, CodeEditorStatus):
        CodeEditorStatus.setWindowTitle(_('Form'))
        self.label.setText(_('Command:'))
        self.label_2.setText(_('Input:'))
        self.label_3.setText(_('Output:'))
        self.labelGoToLine.setText(_('Go to line:'))
        self.labelIFind.setText(_('Find:'))
        self.pushButtonIFindNext.setToolTip(_('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:\'Nimbus Mono L\'; font-size:8pt; font-weight:600; font-style:normal;">\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Find Previous</p></body></html>'))
        self.pushButtonIFindNext.setText(_('Next'))
        self.pushButtonIFindPrevious.setText(_('Previous'))
        self.checkBoxIFindCaseSensitively.setText(_('Case Sensitively'))
        self.labelFind.setText(_('Find:'))
        self.labelReplace.setText(_('Replace:'))
        self.pushButtonReplace.setToolTip(_('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:\'Nimbus Mono L\'; font-size:8pt; font-weight:600; font-style:normal;">\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Replace &amp; Find Previous</p></body></html>'))
        self.pushButtonReplace.setText(_('Replace'))
        self.pushButtonReplaceAll.setText(_('Replace &All'))
        self.pushButtonFindPrevious.setText(_('Previous'))
        self.pushButtonFindNext.setToolTip(_('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta name="qrichtext" content="1" /><style type="text/css">\np, li { white-space: pre-wrap; }\n</style></head><body style=" font-family:\'Nimbus Mono L\'; font-size:8pt; font-weight:600; font-style:normal;">\n<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Find Previous</p></body></html>'))
        self.pushButtonFindNext.setText(_('Next'))
        self.labelFindMode.setText(_('Mode:'))
        self.checkBoxFindCaseSensitively.setText(_('Case Sensitively'))
        self.pushButtonFindAll.setText(_('Find All'))
        self.labelLineColumn.setText(_('Line: 0 Column: 0'))
        self.labelTabSize.setText(_('Tab Size'))

from prymatex import resources_rc
