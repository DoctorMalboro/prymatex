# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/support/project.ui'
#
# Created: Fri Nov  9 18:10:45 2012
#      by: PyQt4 UI code generator snapshot-4.9.6-95094339d25b
#
# WARNING! All changes made in this file will be lost!

from prymatex.utils.i18n import ugettext as _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Project(object):
    def setupUi(self, Project):
        Project.setObjectName(_fromUtf8("Project"))
        Project.resize(361, 237)
        self.formLayout_2 = QtGui.QFormLayout(Project)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setSpacing(2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.labelCommand = QtGui.QLabel(Project)
        self.labelCommand.setObjectName(_fromUtf8("labelCommand"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelCommand)
        self.command = QtGui.QPlainTextEdit(Project)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.command.sizePolicy().hasHeightForWidth())
        self.command.setSizePolicy(sizePolicy)
        self.command.setObjectName(_fromUtf8("command"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.command)

        self.retranslateUi(Project)
        QtCore.QMetaObject.connectSlotsByName(Project)

    def retranslateUi(self, Project):
        Project.setWindowTitle(_('Form'))
        self.labelCommand.setText(_('Command(s):'))

