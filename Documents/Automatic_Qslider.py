from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QSlider
from Documents import Public_Properties
from Documents.Public_Properties import window_change_range


class Automatic_Change_Slider(QSlider, QThread):
    """
    QSlider 类自动适应windows屏幕比例
    """
    sig = pyqtSignal()

    def __init__(self, slider: QSlider, pub: Public_Properties):
        super().__init__()
        self.slider = slider
        self.proportion_slider_h = pub.proportion_of_h  # 按钮和窗口的比例
        self.proportion_slider_w = pub.proportion_of_w
        self.window_state_w = self.slider.width()  # win窗口改变尺寸，当窗户尺寸改变时，检测改变的幅度，用于过滤
        self.window_state_h = self.slider.height()

    def slider_change(self, win: QtWidgets):
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
            self.window_state_w = width
            self.window_state_h = height
            self.slider.setGeometry(QtCore.QRect(int(self.slider.geometry().left() * window_change_rate_w),
                                                 int(self.slider.geometry().top() * window_change_rate_h),
                                                 self.proportion_slider_w * width, self.proportion_slider_h * height))
