from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow, QLineEdit, QMessageBox
from PyQt5.QtCore import QSize
from collections import defaultdict

from Database.users import UsersDB
from Database.records import RecordsDB


WIDTH = 1000
HEIGHT = 800
NIGHT_MODE_ON = False

users_db = UsersDB()
records_db = RecordsDB()

users_db.insert("ermachine", "qwerty", "2003-12-16")
#users_db.update_balance("ermachine2", 100993)
#records_db.insert("add", "100")


def move_to_center(window):
    screen = QApplication.desktop().screenGeometry()
    size = window.geometry()
    x = (screen.width() - size.width()) // 2
    y = (screen.height() - size.height()) // 2
    window.move(x, y)


class MainMenu(QMainWindow):
    buttons = defaultdict()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRINGE BANK")
        self.setStyleSheet("background-color: white")
        self.setFixedWidth(WIDTH)
        self.setFixedHeight(HEIGHT)
        move_to_center(self)

        # set main picture
        self.picture = QPixmap('images/main_picture_OFF.jpeg')
        self.label = QLabel(self)
        self.label.setPixmap(self.picture)
        self.label.setGeometry(100, 300, WIDTH - 150, HEIGHT - 401)
        self.label.setScaledContents(True)

        # style sheets for buttons
        # the first index means whether night mode is on or off
        # the second index is related to design of buttons
        self.style_sheets = [[], []]
        self.__fill_style_sheets()

        # set properties for Register button
        self.buttons["Register"] = QPushButton(self)
        self.buttons["Register"].setGeometry(0, 0, 260, 80)
        self.buttons["Register"].move(WIDTH - 730, 10)
        self.buttons["Register"].setText("Register")
        self.buttons["Register"].setStyleSheet(self.style_sheets[0][0])
        self.buttons["Register"].clicked.connect(self.register_button_press)

        self.buttons["Log in"] = QPushButton(self)
        self.buttons["Log in"].setGeometry(0, 0, 260, 80)
        self.buttons["Log in"].move(WIDTH - 440, 10)
        self.buttons["Log in"].setText("Log in")
        self.buttons["Log in"].setStyleSheet(self.style_sheets[0][0])
        self.buttons["Log in"].clicked.connect(self.log_in_button_press)

        self.buttons["Description"] = QPushButton(self)
        self.buttons["Description"].setGeometry(0, 0, 200, 160)
        self.buttons["Description"].move(30, 10)
        self.buttons["Description"].setText("Description")
        self.buttons["Description"].setStyleSheet(self.style_sheets[0][1])
        self.buttons["Description"].clicked.connect(self.description_button_press)

        self.buttons["Night mode"] = QPushButton(self)
        self.buttons["Night mode"].setGeometry(0, 0, 110, 80)
        self.buttons["Night mode"].move(WIDTH - 140, 10)
        self.buttons["Night mode"].setText("Night\nmode")
        self.buttons["Night mode"].setStyleSheet(self.style_sheets[0][2])
        self.buttons["Night mode"].clicked.connect(self.switch_night_mode)

        self.font = defaultdict()
        for button in self.buttons.keys():
            self.font[button] = self.buttons[button].font()
            self.font[button].setPointSize(20)
            self.buttons[button].setFont(self.font[button])

        if NIGHT_MODE_ON:
            self.switch_night_mode()

    def __fill_style_sheets(self):
        # style sheet for Log in and Register buttons, night mode OFF
        self.style_sheets[0].append('''
                                            QPushButton {
                                                background-color: #1c32ff;
                                                width: 75px;
                                                height: 50px;
                                                border-color: navy;
                                                text-align: center;
                                            }
                                            QPushButton:pressed {
                                                background-color: #8d96ff;
                                            }
                                            ''')

        # style sheet for Log in and Register buttons, night mode ON
        self.style_sheets[1].append('''
                                            QPushButton {
                                                background-color: #fffa96;
                                                width: 75px;
                                                height: 50px;
                                                border-color: navy;
                                                text-align: center;
                                            }
                                            QPushButton:pressed {
                                                background-color: #fff3b0;
                                            }
                                            ''')

        # style sheet for Description button, night mode OFF
        self.style_sheets[0].append('''
                                            QPushButton {
                                                background-color: #ffa19f;
                                                width: 75px;
                                                height: 50px;
                                                border-color: navy;
                                                text-align: center;
                                            }
                                            QPushButton:pressed {
                                                background-color: #ffbdb0;
                                            }
                                            ''')

        # style sheet for Description button, night mode ON
        self.style_sheets[1].append('''
                                            QPushButton {
                                                background-color: #ffd6b6;
                                                width: 75px;
                                                height: 50px;
                                                border-color: navy;
                                                text-align: center;
                                            }
                                            QPushButton:pressed {
                                                background-color: #ffe4ca;
                                            }
                                            ''')

        # style sheet for Night mode button, night mode OFF
        self.style_sheets[0].append('''
                                            QPushButton {
                                                background-color: #fff228;
                                                width: 75px;
                                                height: 50px;
                                                border-color: navy;
                                                text-align: center;
                                            }
                                            QPushButton:pressed {
                                                background-color: #fff775;
                                            }
                                            ''')

        # style sheet for Night mode button, night mode ON
        self.style_sheets[1].append('''
                                            QPushButton {
                                                background-color: #161a7a;
                                                width: 75px;
                                                height: 50px;
                                                border-color: navy;
                                                text-align: center;
                                            }
                                            QPushButton:pressed {
                                                background-color: #1a179c;
                                            }
                                            ''')

    def switch_night_mode(self):
        global NIGHT_MODE_ON

        if NIGHT_MODE_ON:
            NIGHT_MODE_ON = False
            self.setStyleSheet("background-color: white")
            self.buttons["Register"].setStyleSheet(self.style_sheets[0][0])
            self.buttons["Log in"].setStyleSheet(self.style_sheets[0][0])
            self.buttons["Description"].setStyleSheet(self.style_sheets[0][1])
            self.buttons["Night mode"].setStyleSheet(self.style_sheets[0][2])
        else:
            NIGHT_MODE_ON = True
            self.setStyleSheet("background-color: #230a2b")
            self.buttons["Register"].setStyleSheet(self.style_sheets[1][0])
            self.buttons["Log in"].setStyleSheet(self.style_sheets[1][0])
            self.buttons["Description"].setStyleSheet(self.style_sheets[1][1])
            self.buttons["Night mode"].setStyleSheet(self.style_sheets[1][2])

    def register_button_press(self):
        self.close()
        self.register_window = RegisterWindow()
        self.register_window.show()

    def log_in_button_press(self):
        self.close()
        self.log_in_window = LogInWindow()
        self.log_in_window.show()

    def description_button_press(self):
        self.close()
        self.description_window = DescriptionWindow()
        self.description_window.show()


class LogInWindow(QWidget):
    buttons = defaultdict()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRINGE BANK")
        self.setStyleSheet("background-color: white")
        self.setFixedWidth(WIDTH)
        self.setFixedHeight(HEIGHT)
        move_to_center(self)

        self.curr_user_name = ""
        self.curr_password = ""

        self.style_sheets = [[], []]
        self.__fill_style_sheets()

        self.buttons["Back"] = QPushButton(self)
        self.buttons["Back"].setGeometry(0, 0, 100, 40)
        self.buttons["Back"].move(20, 10)
        self.buttons["Back"].setStyleSheet(self.style_sheets[0][0])
        self.buttons["Back"].clicked.connect(self.back_button_press)
        self.buttons["Back"].setIcon(QIcon("images/back.png"))
        self.buttons["Back"].setIconSize(QSize(75, 40))

        self.buttons["Log in"] = QPushButton(self)
        self.buttons["Log in"].setGeometry(0, 0, 400, 50)
        self.buttons["Log in"].move((WIDTH - 400) // 2, 430)
        self.buttons["Log in"].setText("Log in")
        self.buttons["Log in"].setStyleSheet(self.style_sheets[0][0])
        self.buttons["Log in"].clicked.connect(self.log_in_button_press)

        self.buttons["Night mode"] = QPushButton(self)
        self.buttons["Night mode"].setGeometry(0, 0, 110, 80)
        self.buttons["Night mode"].move(WIDTH - 140, 10)
        self.buttons["Night mode"].setText("Night\nmode")
        self.buttons["Night mode"].setStyleSheet(self.style_sheets[0][2])
        self.buttons["Night mode"].clicked.connect(self.switch_night_mode)

        # set user_name input field
        self.user_name_label = QLabel('user name: ', self)
        self.user_name_label.setStyleSheet("color: black")
        self.user_name_label.setFixedSize(210, 30)
        self.user_name_label.move((WIDTH - 200) // 2 - 150, 298)
        self.font_user_name_label = self.user_name_label.font()
        self.font_user_name_label.setPointSize(20)
        self.user_name_label.setFont(self.font_user_name_label)

        self.user_name_input = QLineEdit(self)
        self.user_name_input.setText("")
        self.user_name_input.setObjectName("user_name")
        self.user_name_input.setGeometry((WIDTH - 200) // 2, 300, 400, 30)

        # set password input field
        self.password_label = QLabel('password: ', self)
        self.password_label.setStyleSheet("color: black")
        self.password_label.setFixedSize(210, 30)
        self.password_label.move((WIDTH - 200) // 2 - 140, 338)
        self.font_password_label = self.password_label.font()
        self.font_password_label.setPointSize(20)
        self.password_label.setFont(self.font_password_label)

        self.password_input = QLineEdit(self)
        self.password_input.setText("")
        self.password_input.setObjectName("password")
        self.password_input.setGeometry((WIDTH - 200) // 2, 340, 400, 30)
        self.password_input.setEchoMode(2)

        self.font = defaultdict()
        for button in self.buttons.keys():
            self.font[button] = self.buttons[button].font()
            self.font[button].setPointSize(20)
            self.buttons[button].setFont(self.font[button])

        if NIGHT_MODE_ON:
            self.switch_night_mode()

    def switch_night_mode(self):
        global NIGHT_MODE_ON

        if NIGHT_MODE_ON:
            NIGHT_MODE_ON = False
            self.setStyleSheet("background-color: white")
            self.buttons["Log in"].setStyleSheet(self.style_sheets[0][0])
            self.buttons["Back"].setStyleSheet(self.style_sheets[0][1])
            self.buttons["Night mode"].setStyleSheet(self.style_sheets[0][2])

        else:
            NIGHT_MODE_ON = True
            self.setStyleSheet("background-color: #230a2b")
            self.buttons["Log in"].setStyleSheet(self.style_sheets[1][0])
            self.buttons["Back"].setStyleSheet(self.style_sheets[1][1])
            self.buttons["Night mode"].setStyleSheet(self.style_sheets[1][2])

    def __fill_style_sheets(self):
        # style sheet for Back button, night mode OFF
        self.style_sheets[0].append('''
                                            QPushButton {
                                                background-color: #7eff65;
                                                width: 75px;
                                                height: 50px;
                                                border-color: navy;
                                                text-align: center;
                                            }
                                            QPushButton:pressed {
                                                background-color: #99ff87;
                                            }
                                            ''')

        # style sheet for Back button, night mode ON
        self.style_sheets[1].append('''
                                            QPushButton {
                                                background-color: #7eff65;
                                                width: 75px;
                                                height: 50px;
                                                border-color: navy;
                                                text-align: center;
                                            }
                                            QPushButton:pressed {
                                                background-color: #99ff87;
                                            }
                                            ''')

        # style sheet for Description button, night mode OFF
        self.style_sheets[0].append('''
                                            QPushButton {
                                                background-color: #ffa19f;
                                                width: 75px;
                                                height: 50px;
                                                border-color: navy;
                                                text-align: center;
                                            }
                                            QPushButton:pressed {
                                                background-color: #ffbdb0;
                                            }
                                            ''')

        # style sheet for Description button, night mode ON
        self.style_sheets[1].append('''
                                            QPushButton {
                                                background-color: #ffd6b6;
                                                width: 75px;
                                                height: 50px;
                                                border-color: navy;
                                                text-align: center;
                                            }
                                            QPushButton:pressed {
                                                background-color: #ffe4ca;
                                            }
                                            ''')

        # style sheet for Night mode button, night mode OFF
        self.style_sheets[0].append('''
                                            QPushButton {
                                                background-color: #fff228;
                                                width: 75px;
                                                height: 50px;
                                                border-color: navy;
                                                text-align: center;
                                            }
                                            QPushButton:pressed {
                                                background-color: #fff775;
                                            }
                                            ''')

        # style sheet for Night mode button, night mode ON
        self.style_sheets[1].append('''
                                            QPushButton {
                                                background-color: #161a7a;
                                                width: 75px;
                                                height: 50px;
                                                border-color: navy;
                                                text-align: center;
                                            }
                                            QPushButton:pressed {
                                                background-color: #1a179c;
                                            }
                                            ''')

    def back_button_press(self):
        self.close()
        self.main_menu = MainMenu()
        self.main_menu.show()

    def log_in_button_press(self):
        self.curr_user_name = self.user_name_input.text()
        self.curr_password = self.password_input.text()
        if users_db.in_database(self.curr_user_name, self.curr_password):
            print("SUCCESS!!")
        else:
            self.incorrect_input_window = IncorrectInputWindow()
            self.incorrect_input_window.show()


class RegisterWindow(QWidget):
    buttons = defaultdict()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRINGE BANK")
        self.setStyleSheet("background-color: white")
        self.setFixedWidth(WIDTH)
        self.setFixedHeight(HEIGHT)
        move_to_center(self)

        self.curr_user_name = ""
        self.curr_password = ""

        self.style_sheets = [[], []]
        self.__fill_style_sheets()

        self.buttons["Back"] = QPushButton(self)
        self.buttons["Back"].setGeometry(0, 0, 100, 40)
        self.buttons["Back"].move(20, 10)
        self.buttons["Back"].setStyleSheet(self.style_sheets[0][0])
        self.buttons["Back"].clicked.connect(self.back_button_press)
        self.buttons["Back"].setIcon(QIcon("images/back.png"))
        self.buttons["Back"].setIconSize(QSize(75, 40))

        self.buttons["Register"] = QPushButton(self)
        self.buttons["Register"].setGeometry(0, 0, 400, 50)
        self.buttons["Register"].move((WIDTH - 400) // 2, 430)
        self.buttons["Register"].setText("Register")
        self.buttons["Register"].setStyleSheet(self.style_sheets[0][0])
        self.buttons["Register"].clicked.connect(self.log_in_button_press)

        self.buttons["Night mode"] = QPushButton(self)
        self.buttons["Night mode"].setGeometry(0, 0, 110, 80)
        self.buttons["Night mode"].move(WIDTH - 140, 10)
        self.buttons["Night mode"].setText("Night\nmode")
        self.buttons["Night mode"].setStyleSheet(self.style_sheets[0][2])
        self.buttons["Night mode"].clicked.connect(self.switch_night_mode)

        # set user_name input field
        self.user_name_label = QLabel('user name: ', self)
        self.user_name_label.setStyleSheet("color: black")
        self.user_name_label.setFixedSize(210, 30)
        self.user_name_label.move((WIDTH - 200) // 2 - 150, 298)
        self.font_user_name_label = self.user_name_label.font()
        self.font_user_name_label.setPointSize(20)
        self.user_name_label.setFont(self.font_user_name_label)

        self.user_name_input = QLineEdit(self)
        self.user_name_input.setText("")
        self.user_name_input.setObjectName("user_name")
        self.user_name_input.setGeometry((WIDTH - 200) // 2, 300, 400, 30)

        # set password input field
        self.password_label = QLabel('password: ', self)
        self.password_label.setStyleSheet("color: black")
        self.password_label.setFixedSize(210, 30)
        self.password_label.move((WIDTH - 200) // 2 - 140, 338)
        self.font_password_label = self.password_label.font()
        self.font_password_label.setPointSize(20)
        self.password_label.setFont(self.font_password_label)

        self.password_input = QLineEdit(self)
        self.password_input.setText("")
        self.password_input.setObjectName("password")
        self.password_input.setGeometry((WIDTH - 200) // 2, 340, 400, 30)
        self.password_input.setEchoMode(2)

        # set repeat_password input field
        self.user_name_label = QLabel('repeat password: ', self)
        self.user_name_label.setStyleSheet("color: black")
        self.user_name_label.setFixedSize(210, 30)
        self.user_name_label.move((WIDTH - 200) // 2 - 150, 298)
        self.font_user_name_label = self.user_name_label.font()
        self.font_user_name_label.setPointSize(20)
        self.user_name_label.setFont(self.font_user_name_label)

        self.user_name_input = QLineEdit(self)
        self.user_name_input.setText("")
        self.user_name_input.setObjectName("repeat_password")
        self.user_name_input.setGeometry((WIDTH - 200) // 2, 300, 400, 30)

        self.font = defaultdict()
        for button in self.buttons.keys():
            self.font[button] = self.buttons[button].font()
            self.font[button].setPointSize(20)
            self.buttons[button].setFont(self.font[button])

        if NIGHT_MODE_ON:
            self.switch_night_mode()

    def switch_night_mode(self):
        global NIGHT_MODE_ON

        if NIGHT_MODE_ON:
            NIGHT_MODE_ON = False
            self.setStyleSheet("background-color: white")
            self.buttons["Log in"].setStyleSheet(self.style_sheets[0][0])
            self.buttons["Back"].setStyleSheet(self.style_sheets[0][1])
            self.buttons["Night mode"].setStyleSheet(self.style_sheets[0][2])

        else:
            NIGHT_MODE_ON = True
            self.setStyleSheet("background-color: #230a2b")
            self.buttons["Log in"].setStyleSheet(self.style_sheets[1][0])
            self.buttons["Back"].setStyleSheet(self.style_sheets[1][1])
            self.buttons["Night mode"].setStyleSheet(self.style_sheets[1][2])

    def __fill_style_sheets(self):
        # style sheet for Back button, night mode OFF
        self.style_sheets[0].append('''
                                                QPushButton {
                                                    background-color: #7eff65;
                                                    width: 75px;
                                                    height: 50px;
                                                    border-color: navy;
                                                    text-align: center;
                                                }
                                                QPushButton:pressed {
                                                    background-color: #99ff87;
                                                }
                                                ''')

        # style sheet for Back button, night mode ON
        self.style_sheets[1].append('''
                                                QPushButton {
                                                    background-color: #7eff65;
                                                    width: 75px;
                                                    height: 50px;
                                                    border-color: navy;
                                                    text-align: center;
                                                }
                                                QPushButton:pressed {
                                                    background-color: #99ff87;
                                                }
                                                ''')

        # style sheet for Description button, night mode OFF
        self.style_sheets[0].append('''
                                                QPushButton {
                                                    background-color: #ffa19f;
                                                    width: 75px;
                                                    height: 50px;
                                                    border-color: navy;
                                                    text-align: center;
                                                }
                                                QPushButton:pressed {
                                                    background-color: #ffbdb0;
                                                }
                                                ''')

        # style sheet for Description button, night mode ON
        self.style_sheets[1].append('''
                                                QPushButton {
                                                    background-color: #ffd6b6;
                                                    width: 75px;
                                                    height: 50px;
                                                    border-color: navy;
                                                    text-align: center;
                                                }
                                                QPushButton:pressed {
                                                    background-color: #ffe4ca;
                                                }
                                                ''')

        # style sheet for Night mode button, night mode OFF
        self.style_sheets[0].append('''
                                                QPushButton {
                                                    background-color: #fff228;
                                                    width: 75px;
                                                    height: 50px;
                                                    border-color: navy;
                                                    text-align: center;
                                                }
                                                QPushButton:pressed {
                                                    background-color: #fff775;
                                                }
                                                ''')

        # style sheet for Night mode button, night mode ON
        self.style_sheets[1].append('''
                                                QPushButton {
                                                    background-color: #161a7a;
                                                    width: 75px;
                                                    height: 50px;
                                                    border-color: navy;
                                                    text-align: center;
                                                }
                                                QPushButton:pressed {
                                                    background-color: #1a179c;
                                                }
                                                ''')

    def back_button_press(self):
        self.close()
        self.main_menu = MainMenu()
        self.main_menu.show()

    def log_in_button_press(self):
        self.curr_user_name = self.user_name_input.text()
        self.curr_password = self.password_input.text()
        if users_db.in_database(self.curr_user_name, self.curr_password):
            print("SUCCESS!!")
        else:
            self.incorrect_input_window = IncorrectInputWindow()
            self.incorrect_input_window.show()

class DescriptionWindow(QWidget):
    buttons = defaultdict()


class IncorrectInputWindow(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ACCESS ERROR")
        self.setText("User name or password is wrong. Try again.")
        self.setIcon(QMessageBox.Warning)
