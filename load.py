# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# Загрузить обновить очитстить

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import ast


def Converter(mydata):
    def cvt(log):
        try:
            return ast.literal_eval(log)
        except Exception:
            return str(log)

    return tuple(map(cvt, mydata))


def messageBox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

class Ui_MainWindow(object):

    def loaddata(self):
        """Отображение таблицы"""
        dbconfig = {'host': '127.0.0.1',
                    'user': 'wish_u',
                    'password': 'wish_p',
                    'database': 'wDB', }
        import mysql.connector
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        _SQL = """SELECT * FROM log"""
        rows = cursor.execute(_SQL)
        data = cursor.fetchall()
        print(data)
        for row in data:
            self.addTable(Converter(row))

        if log is empty:
                self.messageBox(self, "Таблица пуста", "Данные отстутствуют")
        cursor.close()
        conn.close()


    def addTable(self, columns):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        for i, column in enumerate(columns):
            self.tableWidget.setItem(rowPosition,i,QtWidgets.QTableWidgetItem(str(column)))


    def update_data(self, name, price, link, note):
        dbconfig = {'host': '127.0.0.1',
                    'user': 'wish_u',
                    'password': 'wish_p',
                    'database': 'wDB', }
        import mysql.connector
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        self.execute("""UPDATE log name=%s, price=%s, link=%s, note=%s WHERE ID=%s""",
                     (name, price, link, note, self.tree.set(self.tree.selection()[0], '#1')))
        cursor.close()

        self.loaddata()

    def clear(self):
        """Очистить всю таблицу"""
        dbconfig = {'host': '127.0.0.1',
                    'user': 'wish_u',
                    'password': 'wish_p',
                    'database': 'wDB', }

        import mysql.connector
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        _SQL = """DELETE FROM log"""
        data = cursor.execute(_SQL)
        conn.commit()
        if data:
            self.messagebox(self, "Поздравляю", "Данные удалены")
        cursor.close()
        conn.close()






    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 432)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 651, 311))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(290, 340, 75, 23))
        self.btn_load.setObjectName("btn_load")
        self.btn_load.clicked.connect(self.loaddata)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 370, 150, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.update_data)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 350, 60, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.clear)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_load.setText(_translate("MainWindow", "Загрузить"))
        self.pushButton_5.setText(_translate("MainWindow", "Обновить"))
        self.pushButton_6.setText(_translate("MainWindow", "Очистить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
