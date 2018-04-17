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

Naniwazu = 'C:\難波津いなばくん'
readlist = os.path.join(Naniwazu, 'readlist.txt')
WMPLAYER = "C:/Program Files/Windows Media Player/wmplayer.exe"
DATADIR =  os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")

class Yomiage(QtCore.QThread):

    def __init__(self, ui):
        super().__init__()
        self.KAMITIME = 10
        self.SIMOTIME = 12
        self.MAAI = 2
        self.stopped = False
        self.mutex = QtCore.QMutex()
        self.ui = ui

    def stop(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stopped = True

    def run(self):
        play = self.playSimpleAudio
        selected = self.ui.karutaTable.selectedItems()
        random.seed()
        random.shuffle(selected)
        play(self.kamiNoKuFile('0'), self.KAMITIME + self.SIMOTIME)
        play(self.simoNoKuFile('0'), self.SIMOTIME)
        for item in selected:
            if self.stopped:
                return
            cardNo = item.text().lstrip()
            play(self.kamiNoKuFile(cardNo), self.KAMITIME)
            time.sleep(self.MAAI)
            play(self.simoNoKuFile(cardNo), self.SIMOTIME)
            time.sleep(self.MAAI)
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
        self.initUI()

        self.yomiage = Yomiage(self.ui)

    def initUI(self):
        self.setWindowIcon(QtGui.QIcon(os.path.join(DATADIR, 'picture', 'ogura.ico')))
        for i in range(10):
            for j in range(10):
                item = QTableWidgetItem(str(10*i + j + 1).rjust(5))
                self.ui.karutaTable.setItem(i, j, item)
        self.ui.btnExit.clicked.connect(self.btnExitClicked)
        self.ui.btnStart.clicked.connect(self.start)
        self.ui.btnSave.clicked.connect(self.save)

        selected = self.read()
        indices = self.getIndex(selected)
        self.select(indices)

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
            self.ui.karutaTable.item(i, j).setSelected(True)

    def save(self):
        selected = self.ui.karutaTable.selectedItems()
        random.seed()
        random.shuffle(selected)
        with open(readlist, 'wt') as f:
            for item in selected:
                f.writelines(item.text().lstrip() + '\n')

    def start(self):
        self.yomiage.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = KarutaForm()
    form.show()
    sys.exit(app.exec_())