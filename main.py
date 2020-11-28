import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel

from LOGIN import Logis
from REG import Regis


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_log = False
        uic.loadUi('main.ui', self)
        self.REG.clicked.connect(self.runREG)
        self.LOG.clicked.connect(self.runLOG)

    def runREG(self):
        self.r = Regis(self, "")
        self.r.show()


    def runLOG(self):
        self.l = Logis(self, "")
        self.l.show()


def except_hook(cls, exception, traceback):
        sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = ex
    sys.exit(app.exec_())
