import sys
import codecs
from PyQt5.QtWidgets import QApplication, QWidget, QLayout, QTextEdit, QGridLayout, QPushButton, QLabel, QDialog,QTableWidget,QTableWidgetItem

from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSlot, Qt


parth = "data\\user.txt"
file = open(parth,'r', encoding='utf-8')
file_user = file.read()
file_user = file_user.split('\n')
user = []
for i in range(len(file_user)):
    user.append(file_user[i].split('|'))
print(user)

file.close()




parth="data\\file.txt"
file = open(parth,'r',encoding='utf-8')
file_user = file.read()
file_users = file_user.split('\n')
file.close()

parth = "data\\matrix.txt"
file = open(parth,'r',encoding='utf-8')
file_user = file.read()
file_user = file_user.split('\n')
matrix = []
for i in range(len(file_user)):
    matrix.append(file_user[i].split('|'))
print(matrix)
file.close()

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.move(100,100)

        self.lay = QGridLayout()
        self.labelLogin = QLabel("Enter login:")
        self.textLogin = QTextEdit("Менеджер проектов (администратор)")
        self.labelPass = QLabel("Enter password:")
        self.textPass = QTextEdit("admin")
        self.button = QPushButton("Enter")
        self.button.clicked.connect(self.on_click)

        self.lay.addWidget(self.labelLogin)
        self.lay.addWidget(self.textLogin)
        self.lay.addWidget(self.labelPass)
        self.lay.addWidget(self.textPass)
        self.lay.addWidget(self.button)

        self.setLayout(self.lay)



        self.show()

    def on_click(self):
        login = self.textLogin.toPlainText()
        password = self.textPass.toPlainText()
        flag = False
        boola=''
        current_log = ""
        for i in range(len(user)):
            if(user[i][0]==login):
                current_log = user[i][0]
                if(user[i][1]==password):
                    boola = user[i][2]
                    flag = True

        if(flag):
            self.widj = QDialog()
            self.widj.setGeometry(100, 100, 800, 600)
            self.widj.lay = QGridLayout()
            self.widj.table = QTableWidget()

            self.widj.table.setRowCount(len(user))
            self.widj.table.setColumnCount(len(file_users))

            horHeader=[]
            for i in range(len(file_users)):
                horHeader.append(file_users[i])
            self.widj.table.setHorizontalHeaderLabels(horHeader)

            vertHeader =[]
            for i in range(len(user)):
                vertHeader.append(user[i][0])
            self.widj.table.setVerticalHeaderLabels(vertHeader)

            for i in range(len(user)):
                for j in range(len(file_users)):

                    t = QTableWidgetItem(str(matrix[i][j]))
                    if(boola!='True'):
                        t.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                        self.widj.table.setItem(i, j, t)
                        self.widj.table.item(i, j).setBackground(QColor(230, 230, 230))
                    else:
                        self.widj.table.setItem(i,j,t)





            self.widj.button3 = QPushButton("Проверить, есть ли \n требуемое разрешение \n в определенной ячейке")
            self.widj.button3.clicked.connect(self.on_click3)
            self.widj.lay.addWidget(self.widj.button3, 1, 1)

            self.widj.button4 = QPushButton("Добавить объект")
            self.widj.button4.clicked.connect(self.on_click4)
            self.widj.lay.addWidget(self.widj.button4,2, 1)

            if (boola == 'True'):
                self.widj.button5 = QPushButton("Добавить субъект")
                self.widj.button5.clicked.connect(self.on_click5)
                self.widj.lay.addWidget(self.widj.button5, 3, 1)

            self.widj.button6 = QPushButton("Удалить объект")
            self.widj.button6.clicked.connect(self.on_click6)
            self.widj.lay.addWidget(self.widj.button6, 4, 1)
            if(boola == 'True'):
                self.widj.button7 = QPushButton("Удалить субъект")
                self.widj.button7.clicked.connect(self.on_click7)
                self.widj.lay.addWidget(self.widj.button7, 5, 1)

            self.widj.button8 = QPushButton("Передача прав")
            self.widj.button8.clicked.connect(self.on_click8)
            self.widj.lay.addWidget(self.widj.button8, 6, 1)

            self.widj.button1 = QPushButton("Сохранить изменения \n в матрице")
            self.widj.button1.clicked.connect(self.on_click2)
            self.widj.lay.addWidget(self.widj.button1, 8, 1)

            self.widj.button9 = QPushButton("Выполнить")
            self.widj.button9.clicked.connect(self.on_click9)
            self.widj.lay.addWidget(self.widj.button9, 7, 1)

            self.widj.lay.addWidget(self.widj.table,0,0)



            self.widj.setLayout(self.widj.lay)
            self.widj.show()
        else:
            self.widj = QDialog()
            self.widj.setGeometry(100, 100, 200, 100)
            label = QLabel("Error!",self.widj)
            label.move(50,50)
            self.widj.show()
    #проверка прав
    def on_click3(self):
        self.widj3 = QDialog()
        self.widj3.setGeometry(100, 100, 400, 300)
        self.widj3.lay = QGridLayout()
        self.widj3.label_user = QLabel("Введите имя субъекта:")
        self.widj3.user = QTextEdit()
        self.widj3.label_obj = QLabel("Введите имя объекта:")
        self.widj3.obj = QTextEdit()
        self.widj3.label_r = QLabel("Введите право (r,w,e):")
        self.widj3.r = QTextEdit()
        self.widj3.label_res = QLabel("Результат проверки:")
        self.widj3.res = QTextEdit()


        self.widj3.button = QPushButton("Проверить")
        self.widj3.button.clicked.connect(self.on_cli)
        self.widj3.lay.addWidget(self.widj3.label_user)
        self.widj3.lay.addWidget(self.widj3.user)
        self.widj3.lay.addWidget(self.widj3.label_obj)
        self.widj3.lay.addWidget(self.widj3.obj)
        self.widj3.lay.addWidget(self.widj3.label_r)
        self.widj3.lay.addWidget(self.widj3.r)
        self.widj3.lay.addWidget(self.widj3.label_res)
        self.widj3.lay.addWidget(self.widj3.res)
        self.widj3.lay.addWidget(self.widj3.button)
        self.widj3.setLayout(self.widj3.lay)
        self.widj3.show()
        print(1)
    #проверка прав
    def on_cli(self):
        w_user = self.widj3.user.toPlainText()
        w_obj = self.widj3.obj.toPlainText()
        w_r = self.widj3.r.toPlainText()
        k=0
        l=0
        for i in range(len(user)):
            if(w_user==user[i][0]):
                k=i
                break
        for i in range(len(file_users)):
            if(w_obj==file_users[i]):
                l=i
                break
        result = matrix[k][l]
        for i in range(len(result)):

            if(result[i]==w_r):

                self.widj3.res.setText("Есть")
                return

        self.widj3.res.setText("Нет")
        print(1)
    #добавить объект
    def on_click4(self):
        self.widj4 = QDialog()
        self.widj4.setGeometry(100, 100, 400, 300)
        self.widj4.lay = QGridLayout()

        self.widj4.label_obj = QLabel("Введите имя объекта:")
        self.widj4.obj = QTextEdit()

        self.widj4.button = QPushButton("Добавить")
        self.widj4.button.clicked.connect(self.add)

        self.widj4.lay.addWidget(self.widj4.label_obj)
        self.widj4.lay.addWidget(self.widj4.obj)
        self.widj4.lay.addWidget(self.widj4.button)

        self.widj4.setLayout(self.widj4.lay)


        self.widj4.show()
        print(1)
    #добавить объект
    def add(self):

        parth = "data\\file.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_users = file_user.split('\n')
        file_users.append(self.widj4.obj.toPlainText())
        file.close()
        file = open(parth, 'w', encoding='utf-8')
        file.write("")
        for i in range(len(file_users)):
            if(i != len(file_users)-1):
                file.write(file_users[i]+"\n")
            else:
                file.write(file_users[i])
        file.close()

        login = self.textLogin.toPlainText()
        password = self.textPass.toPlainText()

        current_log = ""

        for i in range(len(user)):
            if (user[i][0] == login):
                current_log = i


        self.widj.table.insertColumn(len(file_users) - 1)
        self.widj.table.setHorizontalHeaderItem(len(file_users) - 1, QTableWidgetItem(self.widj4.obj.toPlainText()))


        boola = user[current_log][2]
        for i in range(len(user)):
            t = QTableWidgetItem("")
            #self.widj.table.setItem(i, len(file_users)-1, t)
            if (boola != 'True'):
                t.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                #self.widj.table.item(i, len(file_users)-1).setBackground(QColor(230, 230, 230))
            self.widj.table.setItem(i, len(file_users) - 1, t)
            if (boola != 'True'):
                #t.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.widj.table.item(i, len(file_users)-1).setBackground(QColor(230, 230, 230))

        t = QTableWidgetItem("o,w,r,e")
        if (boola != 'True'):
            t.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.widj.table.setItem(current_log, len(file_users) - 1, t)

        if (boola != 'True'):
            self.widj.table.item(current_log, len(file_users) - 1).setBackground(QColor(230, 230, 230))

        parth2 = "data\\matrix.txt"
        file2 = open(parth2, 'w', encoding='utf-8')
        texts = []
        for i in range(len(user)):
            texts.append([])
            for j in range(len(file_users)):
                texts[i].append(self.widj.table.item(i, j).text())

        print(texts)
        result = []
        for i in range(len(texts)):
            str = ""
            for j in range(len(texts[i])):
                if (j != len(texts[i]) - 1):
                    str += texts[i][j] + "|"
                else:
                    str += texts[i][j]
            if (i != len(texts) - 1):
                str += "\n"
            result.append(str)

        print(result)
        file2.write("")
        for i in range(len(result)):
            file2.write(result[i])

        file2.close()

        print(1)
    #добавить субъект
    def on_click5(self):
        self.widj5 = QDialog()
        self.widj5.setGeometry(100, 100, 400, 300)
        self.widj5.lay = QGridLayout()

        self.widj5.label_sub = QLabel("Введите имя субъекта:")
        self.widj5.sub = QTextEdit()

        self.widj5.label_sub_pass = QLabel("Введите пароль субъекта:")
        self.widj5.sub_pass = QTextEdit()

        self.widj5.button = QPushButton("Добавить")
        self.widj5.button.clicked.connect(self.add_sub)

        self.widj5.lay.addWidget(self.widj5.label_sub)
        self.widj5.lay.addWidget(self.widj5.sub)
        self.widj5.lay.addWidget(self.widj5.label_sub_pass)
        self.widj5.lay.addWidget(self.widj5.sub_pass)
        self.widj5.lay.addWidget(self.widj5.button)

        self.widj5.setLayout(self.widj5.lay)

        self.widj5.show()
        print(1)
    #добавить субъект
    def add_sub(self):
        parth = "data\\user.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_user = file_user.split('\n')
        user = []
        for i in range(len(file_user)):
            user.append(file_user[i].split('|'))
        file.close()
        user.append([self.widj5.sub.toPlainText(),self.widj5.sub_pass.toPlainText(),'False'])

        file = open(parth, 'w', encoding='utf-8')
        file.write("")
        result = []
        for i in range(len(user)):
            str = ""
            for j in range(len(user[i])):
                if (j != len(user[i]) - 1):
                    str += user[i][j] + "|"
                else:
                    str += user[i][j]
            if (i != len(user) - 1):
                str += "\n"
            result.append(str)

        for i in range(len(result)):
            file.write(result[i])
        file.close()

        self.widj.table.insertRow(len(user) - 1)
        self.widj.table.setVerticalHeaderItem(len(user) - 1, QTableWidgetItem(self.widj5.sub.toPlainText()))

        login = self.textLogin.toPlainText()
        password = self.textPass.toPlainText()

        parth = "data\\file.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_users = file_user.split('\n')
        file.close()

        for i in range(len(file_users)):
            t = QTableWidgetItem("")
            self.widj.table.setItem(len(user) - 1, i, t)

        self.widj.table.setItem(len(user) - 1, 0, QTableWidgetItem("co,do"))
        parth2 = "data\\matrix.txt"
        file2 = open(parth2, 'w', encoding='utf-8')
        texts = []
        for i in range(len(user)):
            texts.append([])
            for j in range(len(file_users)):
                texts[i].append(self.widj.table.item(i, j).text())

        print(texts)
        result = []
        for i in range(len(texts)):
            str = ""
            for j in range(len(texts[i])):
                if (j != len(texts[i]) - 1):
                    str += texts[i][j] + "|"
                else:
                    str += texts[i][j]
            if (i != len(texts) - 1):
                str += "\n"
            result.append(str)

        print(result)
        file2.write("")
        for i in range(len(result)):
            file2.write(result[i])

        file2.close()

        print(1)
    #удалить объект
    def on_click6(self):
        self.widj6 = QDialog()
        self.widj6.setGeometry(100, 100, 400, 300)
        self.widj6.lay = QGridLayout()

        self.widj6.label_obj = QLabel("Введите имя объекта:")
        self.widj6.obj = QTextEdit()


        self.widj6.button = QPushButton("Удалить")
        self.widj6.button.clicked.connect(self.on_del_obj)


        self.widj6.lay.addWidget(self.widj6.label_obj)
        self.widj6.lay.addWidget(self.widj6.obj)

        self.widj6.lay.addWidget(self.widj6.button)
        self.widj6.setLayout(self.widj6.lay)
        self.widj6.show()


        print(1)
    #удалить объект
    def on_del_obj(self):
        del_obj = self.widj6.obj.toPlainText()
        parth = "data\\file.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_users = file_user.split('\n')
        file.close()


        index = -1
        for i in range(len(file_users)):
            if(del_obj==file_users[i]):
                index = i
                break

        parth = "data\\user.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_user = file_user.split('\n')
        user = []
        for i in range(len(file_user)):
            user.append(file_user[i].split('|'))
        print(user)
        file.close()

        login = self.textLogin.toPlainText()
        current_log = ""
        for i in range(len(user)):
            if (user[i][0] == login):
                current_log = i

        result = self.widj.table.item(current_log, index).text()

        if("o" in result):
            self.widj.table.removeColumn(index)

            current_user = []
            for i in range(len(file_users)):
                if (del_obj != file_users[i]):
                    current_user.append(file_users[i])
            parth = "data\\file.txt"
            file = open(parth, 'w', encoding='utf-8')
            file.write("")
            for i in range(len(current_user)):
                if (i != len(current_user) - 1):
                    file.write(current_user[i] + "\n")
                else:
                    file.write(current_user[i])
            file.close()

            parth = "data\\file.txt"
            file = open(parth, 'r', encoding='utf-8')
            file_user = file.read()
            file_users = file_user.split('\n')
            file.close()

            parth2 = "data\\matrix.txt"
            file2 = open(parth2, 'w', encoding='utf-8')
            texts = []
            for i in range(len(user)):
                texts.append([])
                for j in range(len(file_users)):
                    texts[i].append(self.widj.table.item(i, j).text())

            print(texts)
            result = []
            for i in range(len(texts)):
                str = ""
                for j in range(len(texts[i])):
                    if (j != len(texts[i]) - 1):
                        str += texts[i][j] + "|"
                    else:
                        str += texts[i][j]

                if (i != len(texts) - 1):
                    str += "\n"
                result.append(str)

            print(result)
            file2.write("")
            for i in range(len(result)):
                file2.write(result[i])

            file2.close()
        else:
            self.widjError = QDialog()
            self.widjError.setGeometry(100, 100, 400, 300)
            self.widjError.lay = QGridLayout()
            self.widjError.label_user = QLabel("Ошибка, нет права!")

            self.widjError.lay.addWidget(self.widjError.label_user)

            self.widjError.setLayout(self.widjError.lay)
            self.widjError.show()




        print(1)
    #удалить субъект
    def on_click7(self):
        self.widj7 = QDialog()
        self.widj7.setGeometry(100, 100, 400, 300)
        self.widj7.lay = QGridLayout()

        self.widj7.label_obj = QLabel("Введите имя субъекта:")
        self.widj7.obj = QTextEdit()

        self.widj7.button = QPushButton("Удалить")
        self.widj7.button.clicked.connect(self.on_del_sub)

        self.widj7.lay.addWidget(self.widj7.label_obj)
        self.widj7.lay.addWidget(self.widj7.obj)

        self.widj7.lay.addWidget(self.widj7.button)
        self.widj7.setLayout(self.widj7.lay)
        self.widj7.show()

        print(1)
    #удалить субъект
    def on_del_sub(self):
        del_obj = self.widj7.obj.toPlainText()
        parth = "data\\user.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_user = file_user.split('\n')
        user = []
        for i in range(len(file_user)):
            user.append(file_user[i].split('|'))
        print(user)
        file.close()

        index = -1
        current_us = []
        for i in range(len(user)):
            if (del_obj == user[i][0]):
                index = i
                break
            else:
                current_us.append([user[i][0], user[i][1], user[i][2]])


        self.widj.table.removeRow(index)

        file = open(parth, 'w', encoding='utf-8')
        file.write("")
        result = []
        for i in range(len(current_us)):
            str = ""
            for j in range(len(current_us[i])):
                if (j != len(current_us[i]) - 1):
                    str += current_us[i][j] + "|"
                else:
                    str += current_us[i][j]
            if (i != len(current_us) - 1):
                str += "\n"
            result.append(str)

        for i in range(len(result)):
            file.write(result[i])
        file.close()



        parth = "data\\file.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_users = file_user.split('\n')
        file.close()

        parth = "data\\user.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_user = file_user.split('\n')
        user = []
        for i in range(len(file_user)):
            user.append(file_user[i].split('|'))
        print(user)
        file.close()

        parth2 = "data\\matrix.txt"
        file2 = open(parth2, 'w', encoding='utf-8')
        texts = []
        for i in range(len(user)):
            texts.append([])
            for j in range(len(file_users)):
                texts[i].append(self.widj.table.item(i, j).text())

        print(texts)
        result = []
        for i in range(len(texts)):
            str = ""
            for j in range(len(texts[i])):

                if (j != len(texts[i]) - 1):
                    str += texts[i][j] + "|"
                else:
                    str += texts[i][j]
            if (i != len(texts) - 1):
                str += "\n"
            result.append(str)



        print(result)
        file2.write("")
        for i in range(len(result)):
            file2.write(result[i])

        file2.close()

        print(1)
    #обновить матрицу
    def on_click2(self):
        parth = "data\\user.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_user = file_user.split('\n')
        user = []
        for i in range(len(file_user)):
            user.append(file_user[i].split('|'))
        print(user)
        file.close()

        parth = "data\\file.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_users = file_user.split('\n')
        file.close()

        parth2 = "data\\matrix.txt"
        file2 = open(parth2, 'w', encoding='utf-8')
        texts = []
        for i in range(len(user)):
            texts.append([])
            for j in range(len(file_users)):
                texts[i].append(self.widj.table.item(i,j).text())


        print(texts)
        result = []
        for i in range(len(texts)):
            str = ""
            for j in range(len(texts[i])):
                if(j!=len(texts[i])-1):
                    str += texts[i][j]+"|"
                else:
                    str += texts[i][j]
            if(i!=len(texts)-1):
                str+="\n"
            result.append(str)

        print(result)
        file2.write("")
        for i in range(len(result)):
            file2.write(result[i])

        file2.close()
    #передача прав
    def on_click8(self):
        self.widj8 = QDialog()
        self.widj8.setGeometry(100, 100, 400, 300)
        self.widj8.lay = QGridLayout()
        self.widj8.label_user = QLabel("Введите имя субъекта:")
        self.widj8.user = QTextEdit()
        self.widj8.label_obj = QLabel("Введите имя объекта:")
        self.widj8.obj = QTextEdit()
        self.widj8.label_r = QLabel("Введите право (r,w,e):")
        self.widj8.r = QTextEdit()


        self.widj8.button = QPushButton("Передать право")
        self.widj8.button.clicked.connect(self.give_role)
        self.widj8.lay.addWidget(self.widj8.label_user)
        self.widj8.lay.addWidget(self.widj8.user)
        self.widj8.lay.addWidget(self.widj8.label_obj)
        self.widj8.lay.addWidget(self.widj8.obj)
        self.widj8.lay.addWidget(self.widj8.label_r)
        self.widj8.lay.addWidget(self.widj8.r)

        self.widj8.lay.addWidget(self.widj8.button)
        self.widj8.setLayout(self.widj8.lay)
        self.widj8.show()
        print(1)
    def give_role(self):

        sub_name = self.widj8.user.toPlainText()
        obj_name = self.widj8.obj.toPlainText()
        roles = self.widj8.r.toPlainText()

        parth = "data\\user.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_user = file_user.split('\n')
        user = []
        for i in range(len(file_user)):
            user.append(file_user[i].split('|'))
        print(user)
        file.close()

        login = self.textLogin.toPlainText()

        current_log = ""
        komu = ""
        for i in range(len(user)):
            if (user[i][0] == login):
                current_log = i
            if(user[i][0] == sub_name):
                komu = i


        parth = "data\\file.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_users = file_user.split('\n')
        file.close()

        kuda = ""
        for i in range(len(file_users)):
            if(file_users[i] == obj_name):
                kuda = i

        result = self.widj.table.item(current_log,kuda).text()

        if("o" in result):

            t = QTableWidgetItem(roles)
            self.widj.table.setItem(komu, kuda, t)
            self.widj.table.item(komu, kuda).setBackground(QColor(230, 230, 230))
        else:
            self.widjError = QDialog()
            self.widjError.setGeometry(100, 100, 400, 300)
            self.widjError.lay = QGridLayout()
            self.widjError.label_user = QLabel("Ошибка, нет права!")

            self.widjError.lay.addWidget(self.widjError.label_user)

            self.widjError.setLayout(self.widjError.lay)
            self.widjError.show()


        parth2 = "data\\matrix.txt"
        file2 = open(parth2, 'w', encoding='utf-8')
        texts = []
        for i in range(len(user)):
            texts.append([])
            for j in range(len(file_users)):
                texts[i].append(self.widj.table.item(i, j).text())

        print(texts)
        result = []
        for i in range(len(texts)):
            str = ""
            for j in range(len(texts[i])):
                if (j != len(texts[i]) - 1):
                    str += texts[i][j] + "|"
                else:
                    str += texts[i][j]
            if (i != len(texts) - 1):
                str += "\n"
            result.append(str)

        print(result)
        file2.write("")
        for i in range(len(result)):
            file2.write(result[i])

        file2.close()

        print(1)
    # выполнить
    def on_click9(self):
        self.widj9 = QDialog()
        self.widj9.setGeometry(100, 100, 400, 300)
        self.widj9.lay = QGridLayout()

        self.widj9.label_obj = QLabel("Введите имя объекта:")
        self.widj9.obj = QTextEdit()

        self.widj9.button = QPushButton("Выполнить")
        self.widj9.button.clicked.connect(self.done)

        self.widj9.lay.addWidget(self.widj9.label_obj)
        self.widj9.lay.addWidget(self.widj9.obj)

        self.widj9.lay.addWidget(self.widj9.button)
        self.widj9.setLayout(self.widj9.lay)
        self.widj9.show()

        print(1)
        print(1)
    def done(self):

        parth = "data\\user.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_user = file_user.split('\n')
        user = []
        for i in range(len(file_user)):
            user.append(file_user[i].split('|'))
        print(user)
        file.close()

        parth = "data\\file.txt"
        file = open(parth, 'r', encoding='utf-8')
        file_user = file.read()
        file_users = file_user.split('\n')
        file.close()

        login = self.textLogin.toPlainText()
        password = self.textPass.toPlainText()

        current_log = ""

        for i in range(len(user)):
            if (user[i][0] == login):
                current_log = i

        give_log = 1


        for j in range(len(file_users)):
            if('o' in self.widj.table.item(int(current_log), j).text()):
                newstr = self.widj.table.item(int(current_log), j).text().replace('o,','')
                t = QTableWidgetItem(newstr)
                self.widj.table.setItem(give_log, j, t)

        parth2 = "data\\matrix.txt"
        file2 = open(parth2, 'w', encoding='utf-8')
        texts = []
        for i in range(len(user)):
            texts.append([])
            for j in range(len(file_users)):
                texts[i].append(self.widj.table.item(i, j).text())

        print(texts)
        result = []
        for i in range(len(texts)):
            str = ""
            for j in range(len(texts[i])):
                if (j != len(texts[i]) - 1):
                    str += texts[i][j] + "|"
                else:
                    str += texts[i][j]
            if (i != len(texts) - 1):
                str += "\n"
            result.append(str)

        print(result)
        file2.write("")
        for i in range(len(result)):
            file2.write(result[i])

        file2.close()

        print(1)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


