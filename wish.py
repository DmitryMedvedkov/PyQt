# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wishBD.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import ast

from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb
import pymysql

def Converter(mydata):
    def cvt(log):
        try:
            return ast.literal_eval(log)
        except Exception:
            return str(log)

    return tuple(map(cvt, mydata))

class Ui_MainWindow(object):

    def messageBox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setGeometry(300, 300, 300, 350)
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def connectDB(self):
        try:
            dbconfig = {'host': '127.0.0.1',
                        'user': 'wish_u',
                        'password': 'wish_p',
                        'database': 'wDB', }

            import mysql.connector
            mysql.connector.connect(**dbconfig)
            self.messageBox('Соединение', 'Успешно')
        except pymysql.Error as e:
            self.messageBox('Соединение', 'Нет')
            sys.exit(1)

    def log_request(self):
        """Запись в БД"""
        name = self.lineEdit.text()
        price = self.lineEdit_2.text()
        link = self.lineEdit_3.text()
        note = self.lineEdit_4.text()
        dbconfig = {'host': '127.0.0.1',
                    'user': 'wish_u',
                    'password': 'wish_p',
                    'database': 'wDB', }

        import mysql.connector
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        _SQL = """insert into wdb
                (name, price, link, note)
                values
                (%s, %s, %s, %s)"""
        data = cursor.execute(_SQL, (name, price, link, note))
        if (data == None):
            self.messageBox("Поздравляю", "Данные записаны")
        conn.commit()
        cursor.close()
        conn.close()

    def clearing(self):
        """Полностью очищает БД"""
        dbconfig = {'host': '127.0.0.1',
                    'user': 'wish_u',
                    'password': 'wish_p',
                    'database': 'wDB'}
        import mysql.connector
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        _SQL = "DELETE FROM wdb"
        data = cursor.execute(_SQL)
        if (data==None):
            self.messageBox("Таблица пуста", "Данные отстутствуют")
        cursor.close()
        conn.close()

    def addTable(self, columns):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        for i, column in enumerate(columns):
            self.tableWidget.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(column)))

    def loaddata(self):
        """Отображение таблицы"""
        dbconfig = {'host': '127.0.0.1',
                    'user': 'wish_u',
                    'password': 'wish_p',
                    'database': 'wDB', }
        import mysql.connector
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        _SQL = """SELECT * FROM wdb"""
        rows = cursor.execute(_SQL)
        data = cursor.fetchall()
        print(data)
        for row in data:
            self.addTable(Converter(row))
        if (data==None):
            self.messageBox(self, "Таблица пуста", "Данные отстутствуют")

        cursor.close()
        conn.close()

    def update_data(self):
        dbconfig = {'host': '127.0.0.1',
                    'user': 'wish_u',
                    'password': 'wish_p',
                    'database': 'wDB', }
        import mysql.connector
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        _SQL = """UPDATE wdb SET name=%s WHERE ID=%s"""
        rows = cursor.execute(_SQL)
        data = cursor.fetchall()
        print(data)
        for row in data:
            self.addTable(Converter(row))
        cursor.close()
        conn.close()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 60, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 90, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 150, 81, 21))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 39, 81, 21))
        self.label_5.setObjectName("label_5")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 40, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 120, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 150, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 210, 170, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.log_request)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 233, 170, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.connectDB)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 256, 170, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.clearing)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 276, 170, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.loaddata)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 300, 170, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.update_data)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(120, 324, 651, 311))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(320, 0, 230, 21))
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
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Link"))
        self.label_3.setText(_translate("MainWindow", "Price"))
        self.label_4.setText(_translate("MainWindow", "Note"))
        self.label_5.setText(_translate("MainWindow", "ID"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_2.setText(_translate("MainWindow", "Проверка соединения с БД"))
        self.pushButton_3.setText(_translate("MainWindow", "Очистить БД"))
        self.pushButton_4.setText(_translate("MainWindow", "Показать БД"))
        self.pushButton_5.setText(_translate("MainWindow", "Редактировать"))




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
