import sys
from PyQt5.QtGui import QColor, QPainterPath
from PyQt5.QtWidgets import QLabel, QSlider, QHBoxLayout, QWidget, QApplication, QMainWindow
from PyQt5.QtCore import *
from Documents.Automatic_Gaussian_Label import Automatic_change_Label
from Documents.Automatic_Qslider import Automatic_Change_Slider
from Documents.Automatic_Window import Automatic_Change_Window
from Documents.Public_Properties import Public_Object

from Qwigdet.Qslider.qslider import Ui_Form
# #  https://zhuanlan.zhihu.com/p/437737371  有关于滑块的介绍


class Exp_dome(Automatic_Change_Window, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.ant_horizontalSlider = None
        self.ant_verticalSlide = None
        self.org_width, self.org_height = 500, 350  # 设置初始尺寸
        self.Initialize_window()  # 初始化自动窗口

        self.Initialize_slide()
        self.Initialization_label()

    def Initialize_slide(self):

        verticalSlide = self.verticalSlider
        horizontalSlider = self.horizontalSlider

        pub_vertical = Public_Object(main_w=self.width(), main_h=self.height(),
                                     w=verticalSlide.width(), h=verticalSlide.height())
        pub_horizontalSlider = Public_Object(main_w=self.width(), main_h=self.height(),
                                             w=horizontalSlider.width(), h=horizontalSlider.height())

        self.ant_verticalSlide = Automatic_Change_Slider(slider=verticalSlide, pub=pub_vertical)
        self.ant_horizontalSlider = Automatic_Change_Slider(slider=horizontalSlider, pub=pub_horizontalSlider)

        self.ant_verticalSlide.slider.valueChanged.connect(self.valueChange)
        self.ant_horizontalSlider.slider.valueChanged.connect(self.valueChange)

        with open('re_data/qssfile1.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def Initialization_label(self):
        """初始化
        """

        newlabel = self.label
        pub_label = Public_Object(main_w=self.width(), main_h=self.height(), w=newlabel.width(), h=newlabel.height(), )
        self.gauss_label = Automatic_change_Label(label=newlabel, pub=pub_label)
        self.gauss_label.label.setText("this is test text")

    def valueChange(self):
        value1 = 'verticalSlide当前值：%s' % self.ant_verticalSlide.slider.value()
        value2 = 'horizontalSlider当前值：%s' % self.ant_horizontalSlider.slider.value()

        self.gauss_label.label.setText("{}，\n{}".format(value1,value2))

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.ant_horizontalSlider.slider_change(self)
        self.ant_verticalSlide.slider_change(self)
        self.gauss_label.label_change(self)


if __name__ == '__main__':
    # dpi 自适应
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    main = Exp_dome()
    main.show()
    sys.exit(app.exec_())
