# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\karuta.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(450, 661)
        self.frame = QtWidgets.QFrame(mainForm)
        self.frame.setGeometry(QtCore.QRect(0, 0, 451, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.karutaTable = QtWidgets.QTableWidget(self.frame)
        self.karutaTable.setGeometry(QtCore.QRect(0, 0, 451, 601))
        self.karutaTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.karutaTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.karutaTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.karutaTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.karutaTable.setAutoScroll(True)
        self.karutaTable.setAutoScrollMargin(16)
        self.karutaTable.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.karutaTable.setShowGrid(True)
        self.karutaTable.setRowCount(10)
        self.karutaTable.setColumnCount(10)
        self.karutaTable.setObjectName("karutaTable")
        self.karutaTable.horizontalHeader().setVisible(False)
        self.karutaTable.horizontalHeader().setDefaultSectionSize(45)
        self.karutaTable.horizontalHeader().setMinimumSectionSize(31)
        self.karutaTable.verticalHeader().setVisible(False)
        self.karutaTable.verticalHeader().setDefaultSectionSize(60)
        self.btnStart = QtWidgets.QPushButton(mainForm)
        self.btnStart.setGeometry(QtCore.QRect(10, 620, 51, 23))
        self.btnStart.setObjectName("btnStart")
        self.btnSave = QtWidgets.QPushButton(mainForm)
        self.btnSave.setGeometry(QtCore.QRect(130, 620, 51, 23))
        self.btnSave.setObjectName("btnSave")
        self.btnShow = QtWidgets.QPushButton(mainForm)
        self.btnShow.setGeometry(QtCore.QRect(190, 620, 61, 23))
        self.btnShow.setObjectName("btnShow")
        self.btnExit = QtWidgets.QPushButton(mainForm)
        self.btnExit.setGeometry(QtCore.QRect(370, 620, 75, 23))
        self.btnExit.setObjectName("btnExit")
        self.cbPlayer = QtWidgets.QComboBox(mainForm)
        self.cbPlayer.setGeometry(QtCore.QRect(260, 620, 91, 22))
        self.cbPlayer.setObjectName("cbPlayer")
        self.cbPlayer.addItem("")
        self.cbPlayer.addItem("")
        self.cbPlayer.addItem("")
        self.btnStop = QtWidgets.QPushButton(mainForm)
        self.btnStop.setGeometry(QtCore.QRect(70, 620, 51, 23))
        self.btnStop.setObjectName("btnStop")

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "百人一首"))
        self.btnStart.setText(_translate("mainForm", "開始"))
        self.btnSave.setText(_translate("mainForm", "保存"))
        self.btnShow.setText(_translate("mainForm", "歌選択"))
        self.btnExit.setText(_translate("mainForm", "終了"))
        self.cbPlayer.setItemText(0, _translate("mainForm", "SimpleAudio"))
        self.cbPlayer.setItemText(1, _translate("mainForm", "WinSound"))
        self.cbPlayer.setItemText(2, _translate("mainForm", "WMPlayer"))
        self.btnStop.setText(_translate("mainForm", "中止"))

