from PyQt5.QtGui import QPixmap

from src.Windows import windows


def set_style_sheets(window) -> None:
    window.setStyleSheet("background-color: white")
    for button in window.buttons.keys():

        if button == "Back":
            window.buttons[button].setStyleSheet('''
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

        elif button in ("Register", "Log in") and isinstance(window, windows.MainMenu):
            window.buttons[button].setStyleSheet('''
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

        elif button == "Night mode":
            window.buttons[button].setStyleSheet('''
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

        elif button == "Description":
            window.buttons[button].setStyleSheet('''
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

        elif button == "Log in" and isinstance(window, windows.LogInWindow):
            window.buttons[button].setStyleSheet('''
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

        elif button == "Register" and isinstance(window, windows.RegisterWindow):
            window.buttons[button].setStyleSheet('''
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

        elif button == "Confirm":
            window.buttons[button].setStyleSheet('''
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

        elif button in ("Send", "Withdraw", "Deposit", "History") and isinstance(window, windows.AccountMainPage):
            window.buttons[button].setStyleSheet('''
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

    for label in window.labels.keys():
        window.labels[label].setStyleSheet("color: black;")

    for line_edit in window.line_edits.keys():
        window.line_edits[line_edit].setStyleSheet("color: black; background-color: #f7fcc5;")

    if isinstance(window, windows.MainMenu):
        window.labels["Picture"].setPixmap(QPixmap('images/main_picture_OFF.jpeg'))

