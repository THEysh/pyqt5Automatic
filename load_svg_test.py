from PyQt5.QtCore import QByteArray
from PyQt5.QtSvg import QGraphicsSvgItem, QSvgRenderer
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        scene = QGraphicsScene(self)
        view = QGraphicsView(scene)
        self.setCentralWidget(view)
        self.svg_item2 = QGraphicsSvgItem('Qwigdet/Qbutton/re_data/资源 2.svg')
        scene.addItem(self.svg_item2)
        self.svg_item2.setPos(0, 0)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(480, 480)
    w.show()
    sys.exit(app.exec_())