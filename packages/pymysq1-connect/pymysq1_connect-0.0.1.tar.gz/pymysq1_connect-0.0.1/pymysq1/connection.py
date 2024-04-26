"""
import pymysql

class Database:
    try:
        def __init__(self, user, password, host, database):
            self.connection = pymysql.connect(host=host, user=user, password=password, database=database)
            self.cursor = self.connection.cursor()
            print("Успешно")

    except:
        print("!")




import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QRadioButton
from PyQt5.uic import loadUi

from datetime import datetime

from database import Database


class Menu(QMainWindow):
    def __init__(self,waiter_id,second_name,first_name,last_name):
        super(Menu, self).__init__()
        loadUi("ui/order.ui",self)
        self.db = Database(host='localhost', user='root', password='', database='Luch')
        self.pushButton.clicked.connect(self.add_user)
        self.pushButton_2.clicked.connect(self.show_clients)
        self.show_tables()
        self.show_categ()
        self.comboBox.currentIndexChanged.connect(self.show_food)
        self.pushButton_3.clicked.connect(self.add_check)
        self.waiterId = waiter_id
        self.check_inform(second_name,first_name,last_name)
        self.price = 0


    def check_inform(self,second_name,first_name,last_name):
        time = datetime.now()
        self.listWidget.addItems([f"Офицант:{second_name} {first_name} {last_name}\nВремя:{time}"])



    def add_check(self):

        #Прочитать выбраный элемент
        for i in range(self.verticalLayout_2.count()):
            widget = self.verticalLayout_2.itemAt(i).widget()
            if isinstance(widget, QRadioButton) and widget.isChecked():
                food_text = widget.text()
                food = food_text.split("-")[0]
                food_price = food_text.split("-")[2]

                self.listWidget.addItems([f"Блюдо:{food} цена:{food_price}"])


                self.price += int(food_price)

                self.label_11.setText(str(self.price))


    def show_food(self):
        comboId = self.comboBox.currentIndex() + 1
        query = "SELECT name,ingredients,price FROM food WHERE id_categories = %s"
        self.db.cursor.execute(query,(comboId))
        foods = self.db.cursor.fetchall()
        self.db.connection.commit()

        #Очистка layout
        for i in reversed(range(self.verticalLayout_2.count())):
            self.verticalLayout_2.itemAt(i).widget().setParent(None)
        # Добавление в  layout
        for food in foods:
            rb_food = QRadioButton("{}-{}-{}".format(food[0],food[1],food[2]))
            self.verticalLayout_2.addWidget(rb_food)


    def show_categ(self):

        query = "SELECT name FROM food_categories"
        self.db.cursor.execute(query)
        categs = self.db.cursor.fetchall()
        self.db.connection.commit()

        for categ in categs:
            self.comboBox.addItems(categ)

    def show_tables(self):
        query = "SELECT number FROM RestoransTable WHERE is_busy = 0"
        self.db.cursor.execute(query)
        tables = self.db.cursor.fetchall()
        self.db.connection.commit()

        for table in tables:
            rb_tables = QRadioButton("{}".format(table[0]))
            self.gridLayout.addWidget(rb_tables)
    def show_clients(self):
        query = "SELECT id,phone,count FROM clients"
        self.db.cursor.execute(query)
        clients = self.db.cursor.fetchall()
        self.db.connection.commit()

        #Очистка layout
        for i in reversed(range(self.verticalLayout.count())):
            self.verticalLayout.itemAt(i).widget().setParent(None)

        #Вывод в layout
        for client in clients:
            rb_clients = QRadioButton("{}.{} Гостей:{}".format(client[0],client[1],client[2]))
            self.verticalLayout.addWidget(rb_clients)


    def add_user(self):
        phone = self.lineEdit_2.text()
        count =self.lineEdit_3.text()
        count_int = int(count)

        if count_int >= 7:
            QMessageBox.critical(self,"Ошибка","Максимальное количество гостей 6")
        else:
            query = "INSERT INTO clients(phone,count) VALUES(%s,%s)"
            self.db.cursor.execute(query, (phone, count))
            self.db.connection.commit()
            QMessageBox.information(self,"Успешно","Клиент добавлен")


class AutWaiter(QMainWindow):
    def __init__(self):
        super(AutWaiter, self).__init__()
        loadUi("ui/vhodWaiter.ui",self)
        self.pushButton.clicked.connect(self.autWaiter)
        self.db = Database(host='localhost', user='root', password='', database='Luch')


    def autWaiter(self):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()

        query = f"SELECT id,second_name,first_name,last_name,email,password FROM waiter WHERE email ='{email}' AND password = '{password}'"
        self.db.cursor.execute(query)
        result_aut = self.db.cursor.fetchone()
        self.db.connection.commit()




        if result_aut:
            waiter_id = result_aut[0]
            second_name = result_aut[1]
            first_name = result_aut[2]
            last_name = result_aut[3]

            print("Авторизован")
            self.order_menu = Menu(waiter_id,second_name,first_name,last_name)
            self.order_menu.show()


        else:
            QMessageBox.critical(self,"Ошибка","Не правильный логин или пароль")


class VhodWaiter(QMainWindow):
    def __init__(self):
        super(VhodWaiter,self).__init__()
        loadUi("ui/choiceUser.ui",self)
        self.pushButton.clicked.connect(self.vhod)


    def vhod(self):
        self.vhodWaiter = AutWaiter()
        self.vhodWaiter.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VhodWaiter()
    window.show()
    app.exit(app.exec_())



    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    Обновдение данных
UPDATE имя_таблицы
SET имя_поля = новое_значение
WHERE условие;

        Пример:
UPDATE employees
SET salary = 50000
WHERE department = 'IT';

        Удаление:
UPDATE employees
SET salary = NULL
WHERE department = 'HR';
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""