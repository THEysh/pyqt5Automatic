
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QPushButton
from Documents import Public_Properties
from Documents.Public_Properties import window_change_range




class Automatic_Change_button(QPushButton, QThread):
    sig = pyqtSignal()

    def __init__(self, button: QPushButton, pub: Public_Properties):
        super().__init__()
        self.button = button
        self.proportion_button_h = pub.proportion_of_h  # 按钮和窗口的比例
        self.proportion_button_w = pub.proportion_of_w
        self.window_state_w = self.button.width()  # win窗口改变尺寸，当窗户尺寸改变时，检测改变的幅度，用于过滤
        self.window_state_h = self.button.height()

    def button_change(self, win:QtWidgets):
        """
        当 window 窗口变化，调用这个函数改变尺寸
        width,height 为主窗口变化后的 宽和高
        Window_change_rate 窗口变化率
        这些数据能在窗口中直接得到
        """

        width = win.width()
        height = win.height()
        window_change_rate_w = win.window_change_rate_w
        window_change_rate_h = win.window_change_rate_h

        temp_w = window_change_range(self.window_state_w, width)
        temp_h = window_change_range(self.window_state_h, height)

        if temp_w or temp_h:
            # print('test2')
            # print(window_change_rate_w, window_change_rate_h)
            self.window_state_w = width
            self.window_state_h = height

            self.button.setGeometry(QtCore.QRect(int(self.button.geometry().left() * window_change_rate_w),
                                                     int(self.button.geometry().top() * window_change_rate_h),
                                                     int(self.proportion_button_w * width),
                                                     int(self.proportion_button_h * height)))

