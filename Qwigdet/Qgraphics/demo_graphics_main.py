# coding:utf-8
import math
import sys
import random
from PyQt5.QtChart import QChart, QValueAxis, QLineSeries
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from Documents.Antomatic_QtWidgets import Automatic_Change_QtWidget
from Documents.Automatic_Window import Automatic_Change_Window
from Documents.Automatic_button import Automatic_Change_button
from Documents.Public_Properties import Public_Object
from Qwigdet.Qgraphics.uifile import Ui_Form


class Window(Automatic_Change_Window, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mywid1 = None
        self.setupUi(self)
        self.org_width, self.org_height = self.width(), self.height()
        self.Initialize_window()  # 初始化自动窗口
        self.Initialize_QWidget()

    def Initialize_QWidget(self):
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.graphic_change)  # 计时结束调用operate()方法
        self.timer.start(500)  # 设置计时间隔并启动,1秒

        self.graphicsView.setChart(self.setdate())  # 将图片弄进 ui设计的框架里
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        QtWidget1 = self.graphicsView
        pub = Public_Object(main_w=self.width(), main_h=self.width(),
                            w=QtWidget1.width(), h=QtWidget1.height())
        self.mygraphicsView = Automatic_Change_QtWidget(QtWidget1, pub)

    def graphic_change(self):
        self.mygraphicsView.QtWidget.setChart(self.setdate())

    def setdate(self):
        chart = QChart()
        chart.setTitle("测试")
        seri = QLineSeries()
        seri.setName("cos")
        chart.addSeries(seri)
        t = 0
        for i in range(100):
            y = math.cos(t) * random.random()
            seri.append(t, y)
            t += 0.1
        ax = QValueAxis()
        ax.setRange(0, 10)
        ax.setTitleText("x")
        ay = QValueAxis()
        ay.setRange(-1, 1)
        ay.setTitleText("y")
        chart.setAxisX(ax, seri)
        chart.setAxisY(ay, seri)
        return chart

    def resizeEvent(self, e) -> None:
        super().resizeEvent(e)

        self.mygraphicsView.QtWidget_change(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
