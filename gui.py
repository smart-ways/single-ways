# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Fri Apr 15 10:47:55 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SmartWays(object):
    def setupUi(self, SmartWays):
        SmartWays.setObjectName(_fromUtf8("SmartWays"))
        SmartWays.setWindowModality(QtCore.Qt.NonModal)
        SmartWays.resize(620, 454)
        self.centralwidget = QtGui.QWidget(SmartWays)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnReadCityData = QtGui.QPushButton(self.centralwidget)
        self.btnReadCityData.setGeometry(QtCore.QRect(20, 260, 111, 27))
        self.btnReadCityData.setObjectName(_fromUtf8("btnReadCityData"))
        self.lblHeader = QtGui.QLabel(self.centralwidget)
        self.lblHeader.setGeometry(QtCore.QRect(40, 20, 501, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblHeader.setFont(font)
        self.lblHeader.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHeader.setObjectName(_fromUtf8("lblHeader"))
        self.btnReadTrafficData = QtGui.QPushButton(self.centralwidget)
        self.btnReadTrafficData.setGeometry(QtCore.QRect(220, 260, 121, 27))
        self.btnReadTrafficData.setObjectName(_fromUtf8("btnReadTrafficData"))
        self.btnProcess = QtGui.QPushButton(self.centralwidget)
        self.btnProcess.setGeometry(QtCore.QRect(420, 260, 121, 27))
        self.btnProcess.setObjectName(_fromUtf8("btnProcess"))
        self.lblProcessing = QtGui.QLabel(self.centralwidget)
        self.lblProcessing.setGeometry(QtCore.QRect(250, 180, 241, 17))
        self.lblProcessing.setText(_fromUtf8(""))
        self.lblProcessing.setObjectName(_fromUtf8("lblProcessing"))
        SmartWays.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SmartWays)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SmartWays.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SmartWays)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SmartWays.setStatusBar(self.statusbar)

        self.retranslateUi(SmartWays)
        QtCore.QMetaObject.connectSlotsByName(SmartWays)

    def retranslateUi(self, SmartWays):
        SmartWays.setWindowTitle(_translate("SmartWays", "Smart Ways", None))
        self.btnReadCityData.setText(_translate("SmartWays", "Read City Data", None))
        self.lblHeader.setText(_translate("SmartWays", "SMART WAYS", None))
        self.btnReadTrafficData.setText(_translate("SmartWays", "Read Traffic Data", None))
        self.btnProcess.setText(_translate("SmartWays", "Process", None))

