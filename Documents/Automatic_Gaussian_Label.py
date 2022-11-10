import threading
import cv2
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QLabel

from Documents.GuassFilter import Gauss_b
from Documents.Public_Properties import Public_Object, window_change_range


class Automatic_change_Label(QLabel, QThread):
    sig = pyqtSignal(str)

    def __init__(self, label: QLabel, pub: Public_Object):
        super().__init__()

        self.qrc_imagePath = pub.qrc_imagePath
        self.imagePath = pub.imagePath
        self.label = label
        self.proportion_label_h = pub.proportion_of_h  # 主窗口与label的高的比例
        self.proportion_label_w = pub.proportion_of_w  # 主窗口与label的宽的比例
        self.is_gauss = False
        self.label.setScaledContents(True)  # 自适应尺寸
        self.window_state_w = self.label.width()  # win窗口改变尺寸，当窗户尺寸改变时，检测改变的幅度，用于过滤
        self.window_state_h = self.label.height()

    def emission_signal(self, kerne=40):
        """
        :param  kerne: 0--100之间，越大越模糊
         调用此函数 发射信号并开始异步 渲染高斯模糊，结束后发出信号，信号中装有一个 QPixmap 的值
        """
        if self.is_gauss:
            qrc_imagePath = self.qrc_imagePath
            self.label.setPixmap(QtGui.QPixmap(qrc_imagePath))
            self.is_gauss = False
        else:
            self.kerne = kerne
            sig_threading = threading.Thread(target=Gauss_b,
                                             args=(self.imagePath,self.sig,))
            sig_threading.start()

    def label_change(self, win:QtWidgets):
        """
        width,height 为主窗口 宽和高
        当 window 窗口变化，这个函数改变标签的尺寸
        """
        # width = win.width()
        # height = win.height()
        # self.label.resize(int(width * self.proportion_label_w),
        #                   int(height * self.proportion_label_h))
        width, height = win.width(), win.height()
        window_change_rate_w = win.window_change_rate_w
        window_change_rate_h = win.window_change_rate_h

        temp_w = window_change_range(self.window_state_w, width)
        temp_h = window_change_range(self.window_state_h, height)

        if temp_w or temp_h:
            self.window_state_w = width
            self.window_state_h = height
            self.label.setGeometry(QtCore.QRect(int(self.label.geometry().left() * window_change_rate_w),
                                                 int(self.label.geometry().top() * window_change_rate_h),
                                                 self.proportion_label_w * width, self.proportion_label_h * height))

if __name__ == "main":
    pass
