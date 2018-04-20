# -*- coding: utf-8 -*-
"""
Created on Fri May  5 23:03:36 2017

@author: suzumitu
"""

import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QWidget, QTableWidgetItem, QApplication)
from PyQt5 import QtCore
from naniwazuUI import karuta_form

import os
import fileinput
import random
import simpleaudio as sa
import winsound as ws
import time
import subprocess
import re

WMPLAYER = "C:/Program Files/Windows Media Player/wmplayer.exe"
DATADIR =  os.path.join(os.path.abspath(os.path.dirname(__file__)), "naniwazu_data")
readlist = os.path.join(DATADIR, 'readlist.txt')

class Yomiage(QtCore.QThread):

    def __init__(self, ui):
        super().__init__()
        self.KAMITIME = 10        # only used for WMPlayer
        self.SIMOTIME = 12        # only used for WMPlayer
        self.MAAI_inside = 2      # interval between kaminoku and simonoku
        self.MAAI_outside = 3     # interval between two songs
        self.stopped = False
        self.mutex = QtCore.QMutex()
        self.ui = ui

    def stop(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stopped = True

    def run(self):
        player = self.ui.cbPlayer.currentText()
        if player == 'WinSound':
            play = self.playWinSound
        elif player == 'WMPlayer':
            play = self.playWmPlayer
        else:
            play = self.playSimpleAudio

        selected = self.ui.karutaTable.selectedItems()
        random.seed()
        random.shuffle(selected)

        self.stopped = False
        play(self.kamiNoKuFile('0'), self.KAMITIME + self.SIMOTIME)
        play(self.simoNoKuFile('0'), self.SIMOTIME)
        for item in selected:
            cardNo = re.sub(r'\*(\d+)', r'\1', item.text().lstrip())
            if self.stopped:
                break
            play(self.kamiNoKuFile(cardNo), self.KAMITIME)
            time.sleep(self.MAAI_inside)
            if self.stopped:
                break
            play(self.simoNoKuFile(cardNo), self.SIMOTIME)
            time.sleep(self.MAAI_outside)
        self.stop()
        self.finished.emit()

    def kamiNoKuFile(self, cardNo):
        fileName = 'I-' + format(cardNo, '0>3') + 'A.wav'
        return fileName

    def simoNoKuFile(self, cardNo):
        fileName = 'I-' + format(cardNo, '0>3') + 'B.wav'
        return fileName

    def playSimpleAudio(self, fileName, timeout = 0):
        pathName = os.path.join(DATADIR, fileName)
        wave = sa.WaveObject.from_wave_file(pathName)
        play = wave.play()
        play.wait_done()

    def playWinSound(self, fileName, timeout = 0):
        pathName = os.path.join(DATADIR, fileName)
        ws.PlaySound(pathName, ws.SND_ALIAS)

    def playWmPlayer(self, fileName, timeout):
        try:
            pathName = os.path.join(DATADIR, fileName)
            subprocess.run([WMPLAYER, pathName], timeout=timeout)
        except:
            pass

class KarutaForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = karuta_form.Ui_mainForm()
        self.ui.setupUi(self)
        self.yomiage = Yomiage(self.ui)
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QtGui.QIcon(os.path.join(DATADIR, 'picture', 'ogura.ico')))
        #self.setStyleSheet("background-color:DarkSeaGreen")
        background_color = "background-color:rgba(143,188,143,0.9)"  # DarkSeaGreen
        background_color = "QWidget {" + background_color + "}"
        table_background_color = "QTableWidget {" + background_color + "}"
        image = os.path.join(DATADIR, 'picture', 'ogura4.jpg')
        image = re.sub(r'\\','/', image)
        border_image = "border-image:url(" + image + ")" + " 0 0 0 0 stretch stretch"
        border_image = "QFrame#frame{" + border_image + "}"
        spec = background_color + border_image + table_background_color
        self.setStyleSheet(spec)
        rowCount = self.ui.karutaTable.rowCount()
        columnCount =self.ui.karutaTable.columnCount()
        for i in range(rowCount):
            for j in range(columnCount):
                item = QTableWidgetItem(str(columnCount*i + j + 1).rjust(5))
                self.ui.karutaTable.setItem(i, j, item)
        self.ui.btnExit.clicked.connect(self.btnExitClicked)
        self.ui.btnStart.clicked.connect(self.start)
        self.ui.btnStop.clicked.connect(self.stop)
        self.ui.btnShow.clicked.connect(self.showTable)
        self.ui.btnSave.clicked.connect(self.save)
        self.ui.karutaTable.itemSelectionChanged.connect(self.changeItem)
        self.yomiage.finished.connect(self.finish_yomiage)

        selected = self.read()
        indices = self.getIndex(selected)
        self.select(indices)
        self.ui.karutaTable.setVisible(False)

    def btnExitClicked(self):
        self.yomiage.stop()
        self.yomiage.wait()
        self.close()

    def read(self):
        selected = []
        try:
            with open(readlist, 'rt') as f:
                for line in f:
                    selected.append(int(line.strip()))
        except Exception:
            selected = []
        return selected

    def getIndex(self, nums):
        indices = []
        for num in nums:
            num = num - 1
            i = num // 10
            j = num % 10
            indices.append((i, j))
        return indices

    def select(self, indices):
        for i, j in indices:
            item = self.ui.karutaTable.item(i, j)
            item.setSelected(True)

    def save(self):
        selected = self.ui.karutaTable.selectedItems()
        random.seed()
        random.shuffle(selected)
        with open(readlist, 'wt') as f:
            for item in selected:
                content = re.sub(r'\*(\d+)', r'\1', item.text())
                f.writelines(content.lstrip() + '\n')

    def start(self):
        self.ui.btnStart.setEnabled(False)
        self.ui.cbPlayer.setEnabled(False)
        self.yomiage.start()

    def stop(self):
        self.yomiage.stop()
        self.yomiage.wait()
        self.ui.btnStart.setEnabled(True)
        self.ui.cbPlayer.setEnabled(True)

    def finish_yomiage(self):
        self.yomiage.wait()
        self.ui.btnStart.setEnabled(True)
        self.ui.cbPlayer.setEnabled(True)

    def showTable(self):
        if self.ui.karutaTable.isVisible():
            self.ui.karutaTable.setVisible(False)
        else:
            self.ui.karutaTable.setVisible(True)

    def changeItem(self):
        for i in range(self.ui.karutaTable.rowCount()):
            for j in range(self.ui.karutaTable.columnCount()):
                item = self.ui.karutaTable.item(i,j)
                if item.isSelected():
                    content = re.sub(r'\s(\d+)', r'*\1', item.text())
                    item.setText(content)
                else:
                    content = re.sub(r'\*(\d+)', r' \1', item.text())
                    item.setText(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = KarutaForm()
    form.show()
    sys.exit(app.exec_())
