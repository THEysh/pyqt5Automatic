# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import *

from ui_file2 import Ui_Form

class MyWindow(QMainWindow, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.label.setPixmap(QtGui.QPixmap(":/colored/ui/img.png"))
        self.label.setGeometry(QtCore.QRect(0, 0, 540, 360))
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)  # 窗口置顶，无边框，在任务栏不显示图标

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            print(self.pos() + self._endPos)
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        print(e.button())
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
            app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(app.exec_())
# # 步骤1:设定一个定时器
# self.timer = QTimer(self)
# # 步骤2：将定时器信号和槽函数连接起来
# self.timer.timeout.connect(self.hello)
# self.timer.start(500)