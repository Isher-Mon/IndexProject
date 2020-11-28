import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel


class Logis(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('log.ui', self)
        self.OK.clicked.connect(self.check)

    def check(self):
        self.LorN.setText("Введите логин или почту")
        self.LorN_2.setText("Введите пароль")
        lo = self.Nick.text()
        con = sqlite3.connect("pict.sqlite")
        cur = con.cursor()
        m,l,p = "","",""
        for i in cur.execute("SELECT * FROM acc").fetchall():
            m,p,l = i[1],i[2],i[3]
            print(i)
        if ("@" in lo and lo.split("@")[1] == "yandex.ru" and lo in m) or lo != l:
            if p == self.Pas.text():
                self.LorN_2.setText("Успешно")
            else:
                self.LorN_2.setText("Неверный пароль")
        else:
            self.LorN.setText("Неверный формат")
        con.close()


