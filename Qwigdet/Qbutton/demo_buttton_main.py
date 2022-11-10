import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from Documents.Automatic_Window import Automatic_Change_Window
from Documents.Automatic_Gaussian_Label import Automatic_change_Label
from Documents.Public_Properties import Public_Object
from Documents.Automatic_button import Automatic_Change_button
from ui_file1 import Ui_Form
import sys


class Window(Automatic_Change_Window, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.org_width, self.org_height = 300, 330  # 设置初始尺寸
        self.Initialize_window()  # 初始化窗口
        self.Initialization_Background()
        self.Initialization_button()

        with open('re_data/qssfile1.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def Initialization_button(self):
        self.all_buttons = []
        for i in range(9):
            temp_btn = eval('self.pushButton_{}'.format(i + 1), {'self': self})  # 从 1--9
            pub_button = Public_Object(main_w=self.width(), main_h=self.height(),
                                       w=temp_btn.width(), h=temp_btn.height())
            temp_btn = Automatic_Change_button(button=temp_btn, pub=pub_button)
            self.all_buttons.append(temp_btn)

    def Initialization_Background(self):
        """初始化
        """
        image_path = r"Qbutton/re_data/img.png"  # 这个路径从Qbutton开始
        newlabel = self.label
        pub_label = Public_Object(main_w=self.width(), main_h=self.height(), w=newlabel.width(),
                                  h=newlabel.height())
        pub_label.imagePath = image_path
        self.gauss_label = Automatic_change_Label(label=newlabel, pub=pub_label)
        self.gauss_label.sig.connect(self.gauss_sig_fun)  # 高斯滤波信号
        self.gauss_label.emission_signal()

    def gauss_sig_fun(self, gauss_path: str):
        self.gauss_label.label.setPixmap(QtGui.QPixmap(gauss_path))
        self.gauss_label.is_gauss = True

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        print('hello world')

    def resizeEvent(self, e):
        """
        窗口改变事件
        :param e:
        :return:
        """
        super().resizeEvent(e)
        self.gauss_label.label_change(self)
        for btn in self.all_buttons:
            btn.button.setToolTip('不要点我否则我就🥰(*╯3╰)')
            btn.button_change(self)


if __name__ == '__main__':
    # dpi 自适应
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec_())
