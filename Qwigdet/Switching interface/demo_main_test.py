import sys
from PyQt5 import QtCore, QtWidgets


class MainWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)
    switch_window2 = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Window')

        layout = QtWidgets.QGridLayout()

        self.line_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.line_edit)

        self.button = QtWidgets.QPushButton('Switch Window')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button)

        self.button2 = QtWidgets.QPushButton('to log')
        self.button2.clicked.connect(self.tolog)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit(self.line_edit.text())
    def tolog(self):
        self.switch_window2.emit()
        self.close()

class WindowTwo(QtWidgets.QWidget):

    def __init__(self, text):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Window Two')

        layout = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel(text)
        layout.addWidget(self.label)

        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.button)

        self.setLayout(layout)


class Login(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal(str)


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Login')

        layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton('界面1')
        self.button.clicked.connect(self.login)
        self.button2 = QtWidgets.QPushButton('界面2')
        self.button2.clicked.connect(self.login2)

        layout.addWidget(self.button)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def login(self):
        self.switch_window.emit()
        self.close()

    def login2(self):
        self.switch_window2.emit('abc')
        self.close()

class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_main)
        self.login.switch_window2.connect(self.show_window_two)
        self.login.show()

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_window_two)
        self.window.switch_window2.connect(self.show_login)
        self.window.show()

    def show_window_two(self, text):
        self.window_two = WindowTwo(text)
        #self.window.close()
        self.window_two.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
