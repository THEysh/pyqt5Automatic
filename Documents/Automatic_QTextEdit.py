from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QTextEdit, QSlider

from Documents import Public_Properties
from Documents.Public_Properties import window_change_range


class Automatic_change_qtextedit(QSlider, QThread):
    """
    qtextedit 类自动适应windows屏幕比例
    """
    sig = pyqtSignal()

    def __init__(self, qtextedit: QTextEdit, pub: Public_Properties):
        super().__init__()
        self.qtextedit = qtextedit
        self.proportion_qtextedit_h = pub.proportion_of_h  # 按钮和窗口的比例
        self.proportion_qtextedit_w = pub.proportion_of_w
        self.window_state_w = self.qtextedit.width()  # win窗口改变尺寸，当窗户尺寸改变时，检测改变的幅度，用于过滤
        self.window_state_h = self.qtextedit.height()

    def qtextedit_change(self, win: QtWidgets):
        """
        当 window 窗口变化，调用这个函数改变尺寸
        width,height 为主窗口变化后的 宽和高
        Window_change_rate 窗口变化率
        这些数据能在窗口中直接得到
        """

        width, height = win.width(), win.height()
        window_change_rate_w = win.window_change_rate_w
        window_change_rate_h = win.window_change_rate_h

        temp_w = window_change_range(self.window_state_w, width)
        temp_h = window_change_range(self.window_state_h, height)

        if temp_w or temp_h:
            print(width,height)
            self.window_state_w = width
            self.window_state_h = height

            self.qtextedit.setGeometry(QtCore.QRect(int(self.qtextedit.geometry().left() * window_change_rate_w),
                                                 int(self.qtextedit.geometry().top() * window_change_rate_h),
                                                 self.proportion_qtextedit_w * width, self.proportion_qtextedit_h * height))
