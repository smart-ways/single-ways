# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Fri Apr 15 17:32:32 2016
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
        SmartWays.resize(550, 527)
        SmartWays.setStyleSheet(_fromUtf8("background: rgb(139, 221, 255)"))
        self.centralwidget = QtGui.QWidget(SmartWays)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lblHeader = QtGui.QLabel(self.centralwidget)
        self.lblHeader.setGeometry(QtCore.QRect(20, 0, 501, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblHeader.setFont(font)
        self.lblHeader.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblHeader.setStyleSheet(_fromUtf8("background : None"))
        self.lblHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHeader.setObjectName(_fromUtf8("lblHeader"))
        self.lblProcessing = QtGui.QLabel(self.centralwidget)
        self.lblProcessing.setGeometry(QtCore.QRect(140, 90, 241, 31))
        self.lblProcessing.setText(_fromUtf8(""))
        self.lblProcessing.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProcessing.setObjectName(_fromUtf8("lblProcessing"))
        self.horizontalWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(0, 150, 551, 231))
        self.horizontalWidget.setStyleSheet(_fromUtf8("background: url(/home/hunter/workspace/single-ways/Roads.jpg) 0 0 0 0 center center"))
        self.horizontalWidget.setObjectName(_fromUtf8("horizontalWidget"))
        self.btnProcess = QtGui.QPushButton(self.centralwidget)
        self.btnProcess.setGeometry(QtCore.QRect(400, 430, 85, 27))
        self.btnProcess.setMaximumSize(QtCore.QSize(121, 16777215))
        self.btnProcess.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnProcess.setAutoFillBackground(False)
        self.btnProcess.setStyleSheet(_fromUtf8("color: black;\n"
"opacity: 200"))
        self.btnProcess.setFlat(True)
        self.btnProcess.setObjectName(_fromUtf8("btnProcess"))
        self.btnReadTrafficData = QtGui.QPushButton(self.centralwidget)
        self.btnReadTrafficData.setGeometry(QtCore.QRect(205, 430, 113, 27))
        self.btnReadTrafficData.setMaximumSize(QtCore.QSize(121, 16777215))
        self.btnReadTrafficData.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnReadTrafficData.setAutoFillBackground(False)
        self.btnReadTrafficData.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0)"))
        self.btnReadTrafficData.setFlat(True)
        self.btnReadTrafficData.setObjectName(_fromUtf8("btnReadTrafficData"))
        self.btnReadCityData = QtGui.QPushButton(self.centralwidget)
        self.btnReadCityData.setGeometry(QtCore.QRect(40, 430, 99, 27))
        self.btnReadCityData.setMaximumSize(QtCore.QSize(111, 16777215))
        self.btnReadCityData.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnReadCityData.setAutoFillBackground(False)
        self.btnReadCityData.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0)\n"
""))
        self.btnReadCityData.setFlat(True)
        self.btnReadCityData.setObjectName(_fromUtf8("btnReadCityData"))
        self.btnViewCity = QtGui.QPushButton(self.centralwidget)
        self.btnViewCity.setEnabled(False)
        self.btnViewCity.setGeometry(QtCore.QRect(20, 90, 85, 27))
        self.btnViewCity.setFlat(True)
        self.btnViewCity.setObjectName(_fromUtf8("btnViewCity"))
        self.btnViewTraffic = QtGui.QPushButton(self.centralwidget)
        self.btnViewTraffic.setEnabled(False)
        self.btnViewTraffic.setGeometry(QtCore.QRect(430, 90, 85, 27))
        self.btnViewTraffic.setFlat(True)
        self.btnViewTraffic.setObjectName(_fromUtf8("btnViewTraffic"))
        SmartWays.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SmartWays)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SmartWays.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SmartWays)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SmartWays.setStatusBar(self.statusbar)

        self.retranslateUi(SmartWays)
        QtCore.QMetaObject.connectSlotsByName(SmartWays)

    def retranslateUi(self, SmartWays):
        SmartWays.setWindowTitle(_translate("SmartWays", "Smart Ways", None))
        self.lblHeader.setText(_translate("SmartWays", "SMART WAYS", None))
        self.btnProcess.setText(_translate("SmartWays", "Process", None))
        self.btnReadTrafficData.setText(_translate("SmartWays", "Read Traffic Data", None))
        self.btnReadCityData.setText(_translate("SmartWays", "Read City Data", None))
        self.btnViewCity.setText(_translate("SmartWays", "View City", None))
        self.btnViewTraffic.setText(_translate("SmartWays", "View Traffic", None))

