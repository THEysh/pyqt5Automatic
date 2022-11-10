import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, QPoint, QTimer
from PyQt5.QtWidgets import QApplication, QWidget

from Documents.Antomatic_QtWidgets import Automatic_Change_QtWidget
from Documents.Automatic_Window import Automatic_Change_Window
from Documents.Automatic_button import Automatic_Change_button
from Documents.Public_Properties import Public_Object
from from2 import Ui_Form2
from from3 import Ui_Form3

from main1 import Ui_Form


class ChildrenReom(QWidget, Ui_Form2):
    def __init__(self):
        super(ChildrenReom, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)  # 窗口置顶，无边框，在任务栏不显示图标

        self.Initialize_window()
        self.one = self.__Initialize_widget(self.textBrowser)

    def Initialize_window(self):
        self.Correct_size_h, self.Correct_size_w = self.height(), self.width()
        self.proportion_of_windows = float(self.height() / self.width())  # 设置窗口的比例
        self.width_and_length = [[self.height(), self.width()], [self.height(), self.width()]]  # 窗口变化的栈
        self.window_change_rate_h = self.width_and_length[1][0] / self.width_and_length[0][0]  # 窗口h变化率
        self.window_change_rate_w = self.width_and_length[1][1] / self.width_and_length[0][1]  # 窗口w变化率

    def __Initialize_widget(self, wid):
        pub = Public_Object(main_w=self.width(), main_h=self.height(),
                            w=wid.width(), h=wid.height())
        wid_btn = Automatic_Change_QtWidget(wid, pub=pub)
        return wid_btn

    def resizeEvent(self, e) -> None:
        super().resizeEvent(e)
        self.one.QtWidget_change(self)

class ChildrenReom3(QWidget, Ui_Form3):
    def __init__(self):
        super(ChildrenReom3, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)  # 窗口置顶，无边框，在任务栏不显示图标

        self.Initialize_window()
        self.test = self.__Initialize_widget(self.textBrowser)

    def Initialize_window(self):
        self.Correct_size_h, self.Correct_size_w = self.height(), self.width()
        self.proportion_of_windows = float(self.height() / self.width())  # 设置窗口的比例
        self.width_and_length = [[self.height(), self.width()], [self.height(), self.width()]]  # 窗口变化的栈
        self.window_change_rate_h = self.width_and_length[1][0] / self.width_and_length[0][0]  # 窗口h变化率
        self.window_change_rate_w = self.width_and_length[1][1] / self.width_and_length[0][1]  # 窗口w变化率

    def __Initialize_widget(self, wid):
        pub = Public_Object(main_w=self.width(), main_h=self.height(),
                            w=wid.width(), h=wid.height())
        wid_btn = Automatic_Change_QtWidget(wid, pub=pub)
        return wid_btn

    def resizeEvent(self, e) -> None:
        super().resizeEvent(e)
        self.test.QtWidget_change(self)


class Controller(Automatic_Change_Window, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.org_width = self.width()
        self.org_height = self.height()
        self.Initialize_window()  # 初始化自动窗口

        self.btnlists = []
        self.__get_ant_btn()
        self.__set_sigofbtn()

        self.widtimer = QTimer(self)  # 初始化一个定时器，用于更新子界面的位置
        self.widtimer.timeout.connect(self.widtimerfun)
        self.widtimer.start(50)  # 设置计时间隔并启动,x毫秒

        self.ant_wid1 = self.__Initialize_widget1(self.widget1)  # 界面的空模型,用于显示其他界面

        ## 对其他界面建模
        self.allshow = []
        self.child2 = ChildrenReom()
        self.child3 = ChildrenReom3()

    def __set_sigofbtn(self, ):
        self.btnlists[0].button.clicked.connect(self.show_form2)
        self.btnlists[1].button.clicked.connect(self.show_form3)

    def __get_ant_btn(self):
        self.btnlists.append(self.__Initialize_btn(self.pushButton))
        self.btnlists.append(self.__Initialize_btn(self.pushButton_2))
        self.btnlists.append(self.__Initialize_btn(self.pushButton_3))

    def __Initialize_btn(self, btn):
        pub_button = Public_Object(main_w=self.width(), main_h=self.height(),
                                   w=btn.width(), h=btn.height())
        ant_btn = Automatic_Change_button(button=btn, pub=pub_button)
        return ant_btn

    def __Initialize_widget1(self, wid):
        pub_button = Public_Object(main_w=self.width(), main_h=self.height(),
                                   w=wid.width(), h=wid.height())
        wid_btn = Automatic_Change_QtWidget(wid, pub=pub_button)
        return wid_btn

    def widtimerfun(self):
        print(self.ant_wid1.QtWidget.geometry())
        print('test2')
        print(self.child2.geometry())
        toup = self.ant_wid1.QtWidget.geometry().getRect()

        self.child2.setGeometry(self.geometry().left() + toup[0], self.geometry().top() + toup[1], toup[2], toup[3])
        self.child3.setGeometry(self.geometry().left() + toup[0], self.geometry().top() + toup[1], toup[2], toup[3])

    def resizeEvent(self, e):
        super().resizeEvent(e)

        self.ant_wid1.QtWidget_change(self)
        for k in self.btnlists:
            k.button_change(self)

    def show_form2(self):
        print(self.allshow)
        if len(self.allshow) == 0:
            self.child2.show()
            self.allshow.append(self.child2)

        elif self.allshow[0] == self.child2:
            self.allshow[0].close()
            self.allshow.clear()
        else:
            self.allshow[0].close()
            self.allshow.clear()
            self.allshow.append(self.child2)
            self.child2.show()

    def show_form3(self):
        print(self.allshow)
        if len(self.allshow) == 0:
            self.child3.show()
            self.allshow.append(self.child3)

        elif self.allshow[0] == self.child3:
            self.allshow[0].close()
            self.allshow.clear()
        else:
            self.allshow[0].close()
            self.allshow.clear()
            self.allshow.append(self.child3)
            self.child3.show()

def main():
    # dpi 自适应
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    main = Controller()
    main.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
