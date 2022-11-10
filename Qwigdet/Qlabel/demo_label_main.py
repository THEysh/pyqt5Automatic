import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from Documents.Automatic_Window import Automatic_Change_Window
from Documents.Automatic_Gaussian_Label import Automatic_change_Label
from Documents.Public_Properties import Public_Object
from ui_file2 import Ui_Form


# 创建的窗口 设计使之保持固定的比例

class MyMainForm(Ui_Form, Automatic_Change_Window):

    def __init__(self, *args, **kwargs):
        super(MyMainForm, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.org_width, self.org_height = 540, 360  # 设置初始尺寸
        self.Initialize_window()  # 初始化窗口
        self.Initialization_label()

    def Initialization_label(self):
        """初始化
        """
        qrc_image_path = ':/colored/ui/2.jpg'
        image_path = r'Qlabel/ui/2.jpg'

        newlabel = self.label
        pub_label = Public_Object(main_w=self.width(), main_h=self.height(), w=newlabel.width(), h=newlabel.height(), )
        pub_label.imagePath = image_path
        pub_label.qrc_imagePath = qrc_image_path

        self.gauss_label = Automatic_change_Label(label=newlabel, pub=pub_label)
        self.gauss_label.sig.connect(self.gauss_sig_fun)  # 高斯滤波信号

    def gauss_sig_fun(self, gauss_path: str):
        self.gauss_label.label.setPixmap(QtGui.QPixmap(gauss_path))
        self.gauss_label.is_gauss = True

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        print('hello world')
        self.gauss_label.emission_signal()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        print(self.size())
        self.gauss_label.label_change(self)


if __name__ == "__main__":
    # dpi 自适应
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    demo = MyMainForm()
    demo.show()
    sys.exit(app.exec_())
