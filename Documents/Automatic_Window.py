import math
import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QScreen
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QGridLayout
from qframelesswindow import FramelessWindow
from Documents.Public_Properties import Public_Object, window_change_range


# 创建的窗口 设计使之保持固定的比例

class Automatic_Change_Window(FramelessWindow):
    def __init__(self, *args, **kwargs):
        super(Automatic_Change_Window, self).__init__(*args, **kwargs)
        self.org_width, self.org_height = 540,360   # 设置初始尺寸
        self.org_change_rate_w = None
        self.org_change_rate_h = None
        self.window_change_rate_w = None
        self.window_change_rate_h = None
        self.width_and_length = None
        self.proportion_of_windows = None
        self.Correct_size_h = None
        self.Correct_size_w = None
        self.Initialize_window()

    def Initialize_window(self):
        self.resize(self.org_width, self.org_height)
        self.Correct_size_h, self.Correct_size_w = self.org_height, self.org_width
        self.proportion_of_windows = float(self.height() / self.width())  # 设置窗口的比例
        self.width_and_length = [[self.height(), self.width()], [self.height(), self.width()]]  # 窗口变化的栈
        self.window_change_rate_h = self.width_and_length[1][0] / self.width_and_length[0][0]  # 窗口h变化率
        self.window_change_rate_w = self.window_change_rate_h  # 窗口w变化率等于高的变化率

        self.setMinimumWidth(int(self.org_width * 0.5))
        self.setMinimumHeight(int(self.org_width * 0.5 * self.proportion_of_windows))  # 设置窗口最小值 #必须要符合比例

    def __resize_win(self):

        self.updata_rate()
        size_vari = [self.width_and_length[1][0] - self.width_and_length[0][0],
                     self.width_and_length[1][1] - self.width_and_length[0][1]]  # 获得变化尺寸的差值
        # 变化量大于5个像素，才改变窗口尺寸
        if math.fabs(size_vari[0]) > 5 and math.fabs(size_vari[0]) > math.fabs(size_vari[1]):
            self.resize(int(self.height() / self.proportion_of_windows), self.height())

        elif math.fabs(size_vari[1]) > 5 and math.fabs(size_vari[0]) < math.fabs(size_vari[1]):
            self.resize(self.width(), int(self.width() * self.proportion_of_windows))
        else:
            pass


    def updata_rate(self):
        # 因为事件是 快速进行的 所以要进行过滤：变化需要大于x%才更新数据
        self.width_and_length.append([self.height(), self.width()])
        self.width_and_length.pop(0)

        # 窗口变化率 先计算的高的变化，随后宽跟着改变
        # 下面判断高的变化是否大于%x
        h_is_true = window_change_range(self.width_and_length[1][0], self.width_and_length[0][0])
        temp_h = self.width_and_length[1][0] / self.width_and_length[0][0]

        if h_is_true:
            self.window_change_rate_h = temp_h
            self.window_change_rate_w = temp_h


    def resizeEvent(self, e):
        ## 重载 resize 事件
        super().resizeEvent(e)

        if self.isMaximized():
            desktop = QApplication.desktop()
            # 获取显示器分辨率大小,重新最大化事件
            screenRect = desktop.screenGeometry()
            height = screenRect.height()
            width = screenRect.width()
            length = min(width, height)-45
            if self.org_width > self.org_height:
                self.resize(length * self.proportion_of_windows, length)

            else:
                self.resize(length * (1 / self.proportion_of_windows), length)
        else:
            self.__resize_win()

    def get_window_rate(self):
        self.updata_rate()
        return self.window_change_rate_h, self.window_change_rate_w


if __name__ == "__main__":
    # dpi 自适应
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    demo = Automatic_Change_Window()
    demo.show()
    sys.exit(app.exec_())
