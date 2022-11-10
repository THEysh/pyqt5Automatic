# coding:utf-8
import textwrap

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton


class Dialog(QDialog):
    yesSignal = pyqtSignal()
    cancelSignal = pyqtSignal()

    def __init__(self, title: str, content: str, function_yes_or_no=None, parent=None):
        super().__init__(parent, Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        """
        function_yes_or_no 是传入一个实例化对象，里面写了that_yes函数，和that_no函数 和信号
        当交互选择了yes，yesSignal。   that_yes函数 的动作，计算完成后发出信号
        当交互选择了No，cancelSignal。 做出that_no函数 的动作 计算完成后发出动作
        """
        self.resize(300, 200)
        self.setWindowTitle(title)
        self.content = content
        self.titleLabel = QLabel(title, self)
        self.contentLabel = QLabel(content, self)
        self.yesButton = QPushButton('Yes', self)
        self.cancelButton = QPushButton('No', self)
        self.function_yes_or_no = function_yes_or_no
        self.__initWidget()

    def __initWidget(self):
        """ initialize widgets """
        self.yesButton.setFocus()
        self.titleLabel.move(30, 22)
        self.contentLabel.setMaximumWidth(900)
        self.contentLabel.setText('\n'.join(textwrap.wrap(self.content, 51)))
        self.contentLabel.move(30, self.titleLabel.y() + 50)

        self.__setQss()

        # adjust window size
        rect = self.contentLabel.rect()
        w = 60 + rect.right() + self.cancelButton.width()
        h = self.contentLabel.y() + self.contentLabel.height() + self.yesButton.height() + 60
        self.setFixedSize(w, h)

        # connect signal to slot
        self.yesButton.clicked.connect(self.__onYesButtonClicked)
        self.cancelButton.clicked.connect(self.__onCancelButtonClicked)

    def resizeEvent(self, e):
        self.cancelButton.move(self.width() - self.cancelButton.width() - 30,
                               self.height() - self.cancelButton.height() - 30)
        self.yesButton.move(self.cancelButton.x() -
                            self.yesButton.width() - 30, self.cancelButton.y())

    def __onCancelButtonClicked(self):
        self.cancelSignal.emit()
        print('点击了 no')
        if self.function_yes_or_no is not None:
            self.function_yes_or_no.that_no()
        self.deleteLater()

    def __onYesButtonClicked(self):
        self.yesSignal.emit()
        print('点击了 yes')
        if self.function_yes_or_no is not None:
            self.function_yes_or_no.that_yes()
        self.deleteLater()

    def __setQss(self):
        """ set style sheet """
        self.titleLabel.setObjectName("titleLabel")
        self.contentLabel.setObjectName("contentLabel")

        with open('resource/dialog.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

        self.yesButton.adjustSize()
        self.cancelButton.adjustSize()
        self.contentLabel.adjustSize()
