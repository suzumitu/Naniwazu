# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'karuta.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(476, 542)
        self.btnSave = QtWidgets.QPushButton(mainForm)
        self.btnSave.setGeometry(QtCore.QRect(170, 500, 111, 23))
        self.btnSave.setObjectName("btnSave")
        self.btnExit = QtWidgets.QPushButton(mainForm)
        self.btnExit.setGeometry(QtCore.QRect(360, 500, 75, 23))
        self.btnExit.setObjectName("btnExit")
        self.label = QtWidgets.QLabel(mainForm)
        self.label.setGeometry(QtCore.QRect(40, 30, 191, 20))
        self.label.setObjectName("label")
        self.karutaTable = QtWidgets.QTableWidget(mainForm)
        self.karutaTable.setGeometry(QtCore.QRect(40, 70, 401, 401))
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
        self.karutaTable.horizontalHeader().setDefaultSectionSize(40)
        self.karutaTable.verticalHeader().setVisible(False)
        self.karutaTable.verticalHeader().setDefaultSectionSize(40)
        self.btnStart = QtWidgets.QPushButton(mainForm)
        self.btnStart.setGeometry(QtCore.QRect(60, 500, 75, 23))
        self.btnStart.setObjectName("btnStart")

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "百人一首"))
        self.btnSave.setText(_translate("mainForm", "シャッフル・保存"))
        self.btnExit.setText(_translate("mainForm", "終了"))
        self.label.setText(_translate("mainForm", "歌番号を選んでください"))
        self.btnStart.setText(_translate("mainForm", "開始"))

