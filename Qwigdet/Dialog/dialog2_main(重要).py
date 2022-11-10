# coding:utf-8
import sys
import threading
import time
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QThread, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from Documents.Automatic_Window import Automatic_Change_Window
from Documents.Automatic_button import Automatic_Change_button
from Documents.Dialog import Dialog
from Documents.Public_Properties import Public_Object


class YesOrNofuniction(QThread):  # 1.必须继承QThread，还要调用父类
    """
    这个函数用来做，交互后是与否的 一个选择。采用异步计算，防止主界面卡都安排
    """

    signalTest1 = pyqtSignal(str)  # 2. 信号必须放外面

    def __init__(self):
        super().__init__()  # 必须要调用父类 ！！！！！！！！！！！！！！！！
        self.datayes = "创建一个小猫咪"
        self.datano = "不创建小猫咪"

    def that_yes(self):
        signalTest1_threading = threading.Thread(target=self.fun_yes,
                                                 args=('猫咪 1',))
        signalTest1_threading.start()

    def that_no(self):
        signalTest2_threading = threading.Thread(target=self.fun_no,
                                                 args=('错误,猫咪创建失败了',))
        signalTest2_threading.start()

    def fun_yes(self, test: str):
        time.sleep(2)  # 计算复杂内容
        print("名字计算完成")
        self.signalTest1.emit(test)

    def fun_no(self, test: str):
        time.sleep(2)  # 计算复杂内容
        print("名字计算完成")
        self.signalTest1.emit(test)


class Window(Automatic_Change_Window):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.org_width, self.org_height = 700, 380  # 设置初始尺寸
        self.Initialize_window()
        self.Initialize_btn()
        self.about_dialog_something = YesOrNofuniction()  # 3.创建选择的对象。这个实例化对象有 关于交互的所有东西

        self.about_dialog_something.signalTest1.connect(self.cat_name)

        with open('resource/demofile.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def cat_name(self, event_cat_name: str):
        print('猫咪完成，他的名字是' + event_cat_name)

    def Initialize_btn(self):
        btn = QPushButton('点击开始创建猫咪', parent=self)
        btn.setGeometry(QtCore.QRect(btn.geometry().left(), btn.geometry().top(), 300, 50))
        pub_button = Public_Object(main_w=self.width(), main_h=self.height(),
                                   w=btn.width(), h=btn.height())
        self.ant_btn = Automatic_Change_button(button=btn, pub=pub_button)

        self.ant_btn.button.move(200, 500 / 2)
        self.ant_btn.button.clicked.connect(self.showDialog)

    def showDialog(self):
        content = '点击yes将会在传入的实例化对象function_yes_or_no中的that_yes函数，计算猫的名字'
        w = Dialog('创建一只小猫咪！', content, function_yes_or_no=self.about_dialog_something)
        # 4. 最后这个地方 一定要传入 创建好的实例化对象
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
