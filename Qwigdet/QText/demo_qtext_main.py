import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainterPath
from PyQt5.QtWidgets import QLabel, QSlider, QHBoxLayout, QWidget, QApplication, QMainWindow
from Documents.Automatic_QLineEdit import Automatic_change_QLineEdit
from Documents.Automatic_QTextEdit import Automatic_change_qtextedit
from Documents.Automatic_Window import Automatic_Change_Window
from Documents.Public_Properties import Public_Object

from Qwigdet.QText.Qtext import Ui_Form
# #  https://zhuanlan.zhihu.com/p/437737371  有关于滑块的介绍

class Exp_dome(Automatic_Change_Window, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.org_width, self.org_height = 600, 300
        self.Initialize_window()  # 初始化自动窗口
        self.Initialization_QTextEdit()
        self.Initialization_QlineEdit()
    def Initialization_QTextEdit(self):
        """初始化
        """
        textEdit = self.textEdit
        pub_label = Public_Object(main_w=self.width(), main_h=self.height(), w=textEdit.width(), h=textEdit.height(), )
        self.my_textEdit = Automatic_change_qtextedit(textEdit, pub=pub_label)
        self.my_textEdit.qtextedit.setText("my qtextEdit")

    def Initialization_QlineEdit(self):
        lineEdit = self.lineEdit
        pub_label = Public_Object(main_w=self.width(), main_h=self.height(), w=lineEdit.width(), h=lineEdit.height(), )
        self.my_lineEdit = Automatic_change_QLineEdit(lineEdit, pub=pub_label)
        self.my_lineEdit.qlineedit.setText("my qlineEdit")

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.my_textEdit.qtextedit_change(self)
        self.my_lineEdit.qlineedit_change(self)

if __name__ == '__main__':
    # dpi 自适应
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    main = Exp_dome()
    main.show()
    sys.exit(app.exec_())
