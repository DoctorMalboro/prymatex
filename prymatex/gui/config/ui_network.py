# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/network.ui'
#
# Created: Thu Apr 14 14:53:38 2011
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Network(object):
    def setupUi(self, Network):
        Network.setObjectName(_fromUtf8("Network"))
        Network.resize(460, 403)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/resources/actions/document-open-remote.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Network.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Network)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.radioDirect = QtGui.QRadioButton(Network)
        self.radioDirect.setChecked(True)
        self.radioDirect.setObjectName(_fromUtf8("radioDirect"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.radioDirect)
        self.radioAutomatically = QtGui.QRadioButton(Network)
        self.radioAutomatically.setObjectName(_fromUtf8("radioAutomatically"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.radioAutomatically)
        self.radioBasedOnVariables = QtGui.QRadioButton(Network)
        self.radioBasedOnVariables.setObjectName(_fromUtf8("radioBasedOnVariables"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.radioBasedOnVariables)
        self.label_7 = QtGui.QLabel(Network)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_2 = QtGui.QLineEdit(Network)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.radioPAC = QtGui.QRadioButton(Network)
        self.radioPAC.setObjectName(_fromUtf8("radioPAC"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.radioPAC)
        self.label_6 = QtGui.QLabel(Network)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit = QtGui.QLineEdit(Network)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_5 = QtGui.QLabel(Network)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_5)
        self.comboProxyType = QtGui.QComboBox(Network)
        self.comboProxyType.setEnabled(False)
        self.comboProxyType.setObjectName(_fromUtf8("comboProxyType"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.comboProxyType)
        self.label = QtGui.QLabel(Network)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label)
        self.lineProxyAddress = QtGui.QLineEdit(Network)
        self.lineProxyAddress.setEnabled(False)
        self.lineProxyAddress.setObjectName(_fromUtf8("lineProxyAddress"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.lineProxyAddress)
        self.label_2 = QtGui.QLabel(Network)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_2)
        self.spinProxyPort = QtGui.QSpinBox(Network)
        self.spinProxyPort.setEnabled(False)
        self.spinProxyPort.setMinimum(1)
        self.spinProxyPort.setMaximum(65535)
        self.spinProxyPort.setProperty(_fromUtf8("value"), 8080)
        self.spinProxyPort.setObjectName(_fromUtf8("spinProxyPort"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.spinProxyPort)
        self.radioManual = QtGui.QRadioButton(Network)
        self.radioManual.setObjectName(_fromUtf8("radioManual"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.radioManual)
        self.verticalLayout.addLayout(self.formLayout)
        self.groupBox = QtGui.QGroupBox(Network)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineProxyPassword = QtGui.QLineEdit(self.groupBox)
        self.lineProxyPassword.setEnabled(False)
        self.lineProxyPassword.setObjectName(_fromUtf8("lineProxyPassword"))
        self.gridLayout.addWidget(self.lineProxyPassword, 2, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setEnabled(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setEnabled(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 4, 1, 1)
        self.lineProxyUsername = QtGui.QLineEdit(self.groupBox)
        self.lineProxyUsername.setEnabled(False)
        self.lineProxyUsername.setEchoMode(QtGui.QLineEdit.Password)
        self.lineProxyUsername.setObjectName(_fromUtf8("lineProxyUsername"))
        self.gridLayout.addWidget(self.lineProxyUsername, 2, 5, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushTestSettings = QtGui.QPushButton(Network)
        self.pushTestSettings.setObjectName(_fromUtf8("pushTestSettings"))
        self.horizontalLayout.addWidget(self.pushTestSettings)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Network)
        QtCore.QObject.connect(self.radioBasedOnVariables, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_2.setEnabled)
        QtCore.QObject.connect(self.radioPAC, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit.setEnabled)
        QtCore.QObject.connect(self.radioManual, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineProxyAddress.setEnabled)
        QtCore.QObject.connect(self.radioManual, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.spinProxyPort.setEnabled)
        QtCore.QObject.connect(self.radioBasedOnVariables, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.setFocus)
        QtCore.QObject.connect(self.radioPAC, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.setFocus)
        QtCore.QObject.connect(self.radioManual, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineProxyAddress.setFocus)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_4.setEnabled)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineProxyPassword.setEnabled)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_3.setEnabled)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineProxyUsername.setEnabled)
        QtCore.QObject.connect(self.radioManual, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.comboProxyType.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Network)

    def retranslateUi(self, Network):
        Network.setWindowTitle(QtGui.QApplication.translate("Network", "Network Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.radioDirect.setText(QtGui.QApplication.translate("Network", "&Direct connection", None, QtGui.QApplication.UnicodeUTF8))
        self.radioAutomatically.setText(QtGui.QApplication.translate("Network", "Detect &automatically", None, QtGui.QApplication.UnicodeUTF8))
        self.radioBasedOnVariables.setText(QtGui.QApplication.translate("Network", "Based on enviroment &variables", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Network", "Variable name", None, QtGui.QApplication.UnicodeUTF8))
        self.radioPAC.setText(QtGui.QApplication.translate("Network", "Proxy aut&oconfiguration URL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Network", "Proxy URL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Network", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Network", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Network", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.radioManual.setText(QtGui.QApplication.translate("Network", "&Manual Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Network", "Authentication", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Network", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Network", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Network", "User auth?", None, QtGui.QApplication.UnicodeUTF8))
        self.pushTestSettings.setText(QtGui.QApplication.translate("Network", "Test settings", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Network = QtGui.QWidget()
    ui = Ui_Network()
    ui.setupUi(Network)
    Network.show()
    sys.exit(app.exec_())
