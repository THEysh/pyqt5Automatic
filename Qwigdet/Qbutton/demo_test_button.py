# coding:utf-8
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from Documents.Automatic_Window import Automatic_Change_Window
from Documents.Automatic_button import Automatic_Change_button
from Documents.Public_Properties import Public_Object

class Window(Automatic_Change_Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.org_width, self.org_height = 300, 330  # 设置初始尺寸
        self.Initialize_window()  # 初始化自动窗口
        self.Initialize_btn()
        with open('re_data/qssfile2.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def Initialize_btn(self):
        btn = QPushButton('点我', parent=self)
        pub_button = Public_Object(main_w=self.width(), main_h=self.height(),
                                   w=btn.width(), h=btn.height())
        self.ant_btn = Automatic_Change_button(button=btn, pub=pub_button)

        self.ant_btn.button.move(200, 330/2)
        self.ant_btn.button.clicked.connect(lambda: print('按下按钮'))

    def resizeEvent(self, e) -> None:
        super().resizeEvent(e)
        self.ant_btn.button_change(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
