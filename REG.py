import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel



class Regis(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('reg.ui', self)
        self.OK.clicked.connect(self.sd)

    def sd(self):
        lo = self.Nick.text()
        mail = self.Mail.text()
        con = sqlite3.connect("pict.sqlite")
        cur = con.cursor()
        esult = cur.execute("SELECT mail FROM acc")
        login = cur.execute("SELECT log FROM acc")
        pas , rpas = self.Pas.text(), self.RePas.text()
        if ("@" in mail and mail.split("@")[1] == "yandex.ru") and mail not in esult:
            if(lo not in login):
                if(pas == rpas):
                    cur.execute(f"""INSERT INTO acc(mail , pas , log) VALUES('{mail}','{pas}','{lo}')""")
                    con.commit()
                    con.close()
                    self.hide()
                else:
                    self.EPP.setText("Пароли не совпадают")
            else:
                self.L1.setText("Неверный формат")
        else:
            self.EM.setText("Неверный формат")







