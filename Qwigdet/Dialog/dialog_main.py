# coding:utf-8
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

from Documents.Automatic_Window import Automatic_Change_Window
from Documents.Automatic_button import Automatic_Change_button
from Documents.Dialog import Dialog
from Documents.Public_Properties import Public_Object


class Window(Automatic_Change_Window):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.org_width, self.org_height = 540,360  # 设置初始尺寸
        self.Initialize_window()
        self.Initialize_btn()

        with open('resource/demofile.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def Initialize_btn(self):
        btn = QPushButton('移动窗口，我会变大', parent=self)
        btn.setGeometry(QtCore.QRect(btn.geometry().left(), btn.geometry().top(),300, 50))
        pub_button = Public_Object(main_w=self.width(), main_h=self.height(),
                                   w=btn.width(), h=btn.height())
        self.ant_btn = Automatic_Change_button(button=btn, pub=pub_button)

        self.ant_btn.button.move(200, 500 / 2)
        self.ant_btn.button.clicked.connect(self.showDialog)

    def showDialog(self):
        content = '这是一个测试问句，你可以选择是或者否。' \
                  '假设这一局话很长很长很长很长很长很长很长很长' \
                  '很长很长很长很长很长很长很长很长很长很长很长很长' \
                  '很长很长很长很长很长很长很长很长很长很长很长很长'
        w = Dialog('真的很酷！', content)
        w.exec()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.ant_btn.button_change(self)


if __name__ == '__main__':
    # dpi 自适应
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
