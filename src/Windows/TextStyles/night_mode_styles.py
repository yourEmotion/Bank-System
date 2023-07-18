from PyQt5.QtGui import QPixmap

from src.Windows import windows


def set_style_sheets(window) -> None:
    window.setStyleSheet("background-color: #1e0a28")
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

        elif button == "Night mode":
            window.buttons[button].setStyleSheet('''
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

        elif button == "Description":
            window.buttons[button].setStyleSheet('''
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
        window.labels[label].setStyleSheet("color: white;")

    for line_edit in window.line_edits.keys():
        window.line_edits[line_edit].setStyleSheet("color: white; background-color: #520c23;")

    if isinstance(window, windows.MainMenu):
        window.labels["Picture"].setPixmap(QPixmap('images/main_picture_ON.jpeg'))
