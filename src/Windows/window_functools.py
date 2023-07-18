from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QScrollArea, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import QSize

from src.Windows import windows

from collections import defaultdict

from src.Database.records import records_db


WIDTH = 1000
HEIGHT = 800


def move_to_center(window) -> None:
    screen = QApplication.desktop().screenGeometry()
    size = window.geometry()
    x = (screen.width() - size.width()) // 2
    y = (screen.height() - size.height()) // 2
    window.move(x, y)


def set_buttons(window) -> None:

    if isinstance(window, windows.MainMenu):

        window.buttons["Register"] = QPushButton(window)
        window.buttons["Register"].setGeometry(0, 0, 260, 80)
        window.buttons["Register"].move(WIDTH - 730, 10)
        window.buttons["Register"].setText("Register")
        window.buttons["Register"].clicked.connect(window.register_button_press)

        window.buttons["Log in"] = QPushButton(window)
        window.buttons["Log in"].setGeometry(0, 0, 260, 80)
        window.buttons["Log in"].move(WIDTH - 440, 10)
        window.buttons["Log in"].setText("Log in")
        window.buttons["Log in"].clicked.connect(window.log_in_button_press)

        window.buttons["Description"] = QPushButton(window)
        window.buttons["Description"].setGeometry(0, 0, 200, 160)
        window.buttons["Description"].move(30, 10)
        window.buttons["Description"].setText("Description")
        window.buttons["Description"].clicked.connect(window.description_button_press)

        window.buttons["Night mode"] = QPushButton(window)
        window.buttons["Night mode"].setGeometry(0, 0, 110, 80)
        window.buttons["Night mode"].move(WIDTH - 140, 10)
        window.buttons["Night mode"].setText("Night\nmode")
        window.buttons["Night mode"].clicked.connect(window.switch_night_mode)

        window.fonts = defaultdict()
        for button in window.buttons.keys():
            window.fonts[button] = window.buttons[button].font()
            window.fonts[button].setPointSize(20)
            window.buttons[button].setFont(window.fonts[button])

    elif isinstance(window, windows.LogInWindow):

        window.buttons["Back"] = QPushButton(window)
        window.buttons["Back"].setGeometry(0, 0, 100, 40)
        window.buttons["Back"].move(20, 10)
        window.buttons["Back"].clicked.connect(window.back_button_press)
        window.buttons["Back"].setIcon(QIcon("images/back.png"))
        window.buttons["Back"].setIconSize(QSize(75, 40))

        window.buttons["Log in"] = QPushButton(window)
        window.buttons["Log in"].setGeometry(0, 0, 400, 50)
        window.buttons["Log in"].move((WIDTH - 400) // 2, 430)
        window.buttons["Log in"].setText("Log in")
        window.buttons["Log in"].clicked.connect(window.log_in_button_press)

        window.buttons["Night mode"] = QPushButton(window)
        window.buttons["Night mode"].setGeometry(0, 0, 110, 80)
        window.buttons["Night mode"].move(WIDTH - 140, 10)
        window.buttons["Night mode"].setText("Night\nmode")
        window.buttons["Night mode"].clicked.connect(window.switch_night_mode)

        window.fonts = defaultdict()
        for button in window.buttons.keys():
            window.fonts[button] = window.buttons[button].font()
            window.fonts[button].setPointSize(20)
            window.buttons[button].setFont(window.fonts[button])

    elif isinstance(window, windows.RegisterWindow):

        window.buttons["Back"] = QPushButton(window)
        window.buttons["Back"].setGeometry(0, 0, 100, 40)
        window.buttons["Back"].move(20, 10)
        window.buttons["Back"].clicked.connect(window.back_button_press)
        window.buttons["Back"].setIcon(QIcon("images/back.png"))
        window.buttons["Back"].setIconSize(QSize(75, 40))

        window.buttons["Register"] = QPushButton(window)
        window.buttons["Register"].setGeometry(0, 0, 400, 50)
        window.buttons["Register"].move((WIDTH - 400) // 2, 470)
        window.buttons["Register"].setText("Register")
        window.buttons["Register"].clicked.connect(window.register_button_press)

        window.buttons["Night mode"] = QPushButton(window)
        window.buttons["Night mode"].setGeometry(0, 0, 110, 80)
        window.buttons["Night mode"].move(WIDTH - 140, 10)
        window.buttons["Night mode"].setText("Night\nmode")
        window.buttons["Night mode"].clicked.connect(window.switch_night_mode)

        window.fonts = defaultdict()
        for button in window.buttons.keys():
            window.fonts[button] = window.buttons[button].font()
            window.fonts[button].setPointSize(20)
            window.buttons[button].setFont(window.fonts[button])

    elif isinstance(window, windows.DescriptionWindow):

        window.buttons["Back"] = QPushButton(window)
        window.buttons["Back"].setGeometry(0, 0, 100, 40)
        window.buttons["Back"].move(20, 10)
        window.buttons["Back"].clicked.connect(window.back_button_press)
        window.buttons["Back"].setIcon(QIcon("images/back.png"))
        window.buttons["Back"].setIconSize(QSize(75, 40))

        window.buttons["Night mode"] = QPushButton(window)
        window.buttons["Night mode"].setGeometry(0, 0, 110, 80)
        window.buttons["Night mode"].move(WIDTH - 140, 10)
        window.buttons["Night mode"].setText("Night\nmode")
        window.buttons["Night mode"].clicked.connect(window.switch_night_mode)

        window.fonts = defaultdict()
        for button in window.buttons.keys():
            window.fonts[button] = window.buttons[button].font()
            window.fonts[button].setPointSize(20)
            window.buttons[button].setFont(window.fonts[button])

    elif isinstance(window, windows.AccountMainPage):

        window.buttons["Send"] = QPushButton(window)
        window.buttons["Send"].setGeometry(0, 0, 260, 200)
        window.buttons["Send"].move(220, 250)
        window.buttons["Send"].setText("Send money")
        window.buttons["Send"].clicked.connect(window.send_button_press)

        window.buttons["Withdraw"] = QPushButton(window)
        window.buttons["Withdraw"].setGeometry(0, 0, 260, 200)
        window.buttons["Withdraw"].move(520, 250)
        window.buttons["Withdraw"].setText("Withdraw money")
        window.buttons["Withdraw"].clicked.connect(window.withdraw_button_press)

        window.buttons["Deposit"] = QPushButton(window)
        window.buttons["Deposit"].setGeometry(0, 0, 260, 200)
        window.buttons["Deposit"].move(220, 500)
        window.buttons["Deposit"].setText("Deposit money")
        window.buttons["Deposit"].clicked.connect(window.deposit_button_press)

        window.buttons["History"] = QPushButton(window)
        window.buttons["History"].setGeometry(0, 0, 260, 200)
        window.buttons["History"].move(520, 500)
        window.buttons["History"].setText("View transaction\nhistory")
        window.buttons["History"].clicked.connect(window.view_history_button_press)

        window.buttons["Back"] = QPushButton(window)
        window.buttons["Back"].setGeometry(0, 0, 100, 40)
        window.buttons["Back"].move(20, 10)
        window.buttons["Back"].clicked.connect(window.back_button_press)
        window.buttons["Back"].setIcon(QIcon("images/back.png"))
        window.buttons["Back"].setIconSize(QSize(75, 40))

        window.buttons["Night mode"] = QPushButton(window)
        window.buttons["Night mode"].setGeometry(0, 0, 110, 80)
        window.buttons["Night mode"].move(WIDTH - 140, 10)
        window.buttons["Night mode"].setText("Night\nmode")
        window.buttons["Night mode"].clicked.connect(window.switch_night_mode)

        window.fonts = defaultdict()
        for button in window.buttons.keys():
            window.fonts[button] = window.buttons[button].font()
            window.fonts[button].setPointSize(20)
            window.buttons[button].setFont(window.fonts[button])

    elif isinstance(window, windows.SendWindow):

        window.buttons["Confirm"] = QPushButton(window)
        window.buttons["Confirm"].setGeometry(0, 0, 260, 200)
        window.buttons["Confirm"].move((WIDTH - 260) // 2, 500)
        window.buttons["Confirm"].setText("Confirm")
        window.buttons["Confirm"].clicked.connect(window.confirm_button_press)

        window.buttons["Back"] = QPushButton(window)
        window.buttons["Back"].setGeometry(0, 0, 100, 40)
        window.buttons["Back"].move(20, 10)
        window.buttons["Back"].clicked.connect(window.back_button_press)
        window.buttons["Back"].setIcon(QIcon("images/back.png"))
        window.buttons["Back"].setIconSize(QSize(75, 40))

        window.buttons["Night mode"] = QPushButton(window)
        window.buttons["Night mode"].setGeometry(0, 0, 110, 80)
        window.buttons["Night mode"].move(WIDTH - 140, 10)
        window.buttons["Night mode"].setText("Night\nmode")
        window.buttons["Night mode"].clicked.connect(window.switch_night_mode)

        window.fonts = defaultdict()
        for button in window.buttons.keys():
            window.fonts[button] = window.buttons[button].font()
            window.fonts[button].setPointSize(20)
            window.buttons[button].setFont(window.fonts[button])

    elif isinstance(window, windows.DepositWindow):

        window.buttons["Confirm"] = QPushButton(window)
        window.buttons["Confirm"].setGeometry(0, 0, 260, 200)
        window.buttons["Confirm"].move((WIDTH - 260) // 2, 500)
        window.buttons["Confirm"].setText("Confirm")
        window.buttons["Confirm"].clicked.connect(window.confirm_button_press)

        window.buttons["Back"] = QPushButton(window)
        window.buttons["Back"].setGeometry(0, 0, 100, 40)
        window.buttons["Back"].move(20, 10)
        window.buttons["Back"].clicked.connect(window.back_button_press)
        window.buttons["Back"].setIcon(QIcon("images/back.png"))
        window.buttons["Back"].setIconSize(QSize(75, 40))

        window.buttons["Night mode"] = QPushButton(window)
        window.buttons["Night mode"].setGeometry(0, 0, 110, 80)
        window.buttons["Night mode"].move(WIDTH - 140, 10)
        window.buttons["Night mode"].setText("Night\nmode")
        window.buttons["Night mode"].clicked.connect(window.switch_night_mode)

        window.fonts = defaultdict()
        for button in window.buttons.keys():
            window.fonts[button] = window.buttons[button].font()
            window.fonts[button].setPointSize(20)
            window.buttons[button].setFont(window.fonts[button])

    elif isinstance(window, windows.WithdrawWindow):

        window.buttons["Confirm"] = QPushButton(window)
        window.buttons["Confirm"].setGeometry(0, 0, 260, 200)
        window.buttons["Confirm"].move((WIDTH - 260) // 2, 500)
        window.buttons["Confirm"].setText("Confirm")
        window.buttons["Confirm"].clicked.connect(window.confirm_button_press)

        window.buttons["Back"] = QPushButton(window)
        window.buttons["Back"].setGeometry(0, 0, 100, 40)
        window.buttons["Back"].move(20, 10)
        window.buttons["Back"].clicked.connect(window.back_button_press)
        window.buttons["Back"].setIcon(QIcon("images/back.png"))
        window.buttons["Back"].setIconSize(QSize(75, 40))

        window.buttons["Night mode"] = QPushButton(window)
        window.buttons["Night mode"].setGeometry(0, 0, 110, 80)
        window.buttons["Night mode"].move(WIDTH - 140, 10)
        window.buttons["Night mode"].setText("Night\nmode")
        window.buttons["Night mode"].clicked.connect(window.switch_night_mode)

        window.fonts = defaultdict()
        for button in window.buttons.keys():
            window.fonts[button] = window.buttons[button].font()
            window.fonts[button].setPointSize(20)
            window.buttons[button].setFont(window.fonts[button])

    elif isinstance(window, windows.HistoryWindow):

        window.buttons["Back"] = QPushButton(window)
        window.buttons["Back"].setGeometry(0, 0, 100, 40)
        window.buttons["Back"].move(20, 10)
        window.buttons["Back"].clicked.connect(window.back_button_press)
        window.buttons["Back"].setIcon(QIcon("images/back.png"))
        window.buttons["Back"].setIconSize(QSize(75, 40))

        window.buttons["Night mode"] = QPushButton(window)
        window.buttons["Night mode"].setGeometry(0, 0, 110, 80)
        window.buttons["Night mode"].move(WIDTH - 140, 10)
        window.buttons["Night mode"].setText("Night\nmode")
        window.buttons["Night mode"].clicked.connect(window.switch_night_mode)

        window.fonts = defaultdict()
        for button in window.buttons.keys():
            window.fonts[button] = window.buttons[button].font()
            window.fonts[button].setPointSize(20)
            window.buttons[button].setFont(window.fonts[button])

    elif isinstance(window, windows.OperationSuccessWindow):
        
        window.addButton(QMessageBox.Ok)
        window.ok_button = window.button(QMessageBox.Ok)
        window.ok_button.clicked.connect(window.ok_button_press)


def set_labels(window, wrong_field=None) -> None:

    if isinstance(window, windows.MainMenu):
        window.labels["Picture"] = QLabel(window)
        window.labels["Picture"].setGeometry(100, 300, WIDTH - 200, HEIGHT - 400)
        window.labels["Picture"].setScaledContents(True)

    elif isinstance(window, windows.LogInWindow):
        window.labels["User name"] = QLabel('user name: ', window)
        window.labels["User name"].setStyleSheet("color: black")
        window.labels["User name"].setFixedSize(210, 30)
        window.labels["User name"].move((WIDTH - 200) // 2 - 150, 298)

        window.labels["Password"] = QLabel('password: ', window)
        window.labels["Password"].setStyleSheet("color: black")
        window.labels["Password"].setFixedSize(210, 30)
        window.labels["Password"].move((WIDTH - 200) // 2 - 140, 338)

        window.fonts = defaultdict()
        for label in window.labels.keys():
            window.fonts[label] = window.labels[label].font()
            window.fonts[label].setPointSize(20)
            window.labels[label].setFont(window.fonts[label])

    elif isinstance(window, windows.RegisterWindow):

        window.labels["User name"] = QLabel('user name: ', window)
        window.labels["User name"].setStyleSheet("color: black")
        window.labels["User name"].setFixedSize(210, 30)
        window.labels["User name"].move((WIDTH - 200) // 2 - 150, 298)

        window.labels["Birthday"] = QLabel('birthday (DD.MM.YYYY): ', window)
        window.labels["Birthday"].setStyleSheet("color: black")
        window.labels["Birthday"].setFixedSize(300, 30)
        window.labels["Birthday"].move((WIDTH - 200) // 2 - 317, 338)

        window.labels["Password"] = QLabel('password: ', window)
        window.labels["Password"].setStyleSheet("color: black")
        window.labels["Password"].setFixedSize(210, 30)
        window.labels["Password"].move((WIDTH - 200) // 2 - 140, 378)

        window.labels["Repeat password"] = QLabel('repeat password: ', window)
        window.labels["Repeat password"].setStyleSheet("color: black")
        window.labels["Repeat password"].setFixedSize(210, 30)
        window.labels["Repeat password"].move((WIDTH - 200) // 2 - 228, 418)

        window.fonts = defaultdict()
        for label in window.labels.keys():
            window.fonts[label] = window.labels[label].font()
            window.fonts[label].setPointSize(20)
            window.labels[label].setFont(window.fonts[label])

    elif isinstance(window, windows.DescriptionWindow):

        window.fonts = defaultdict()

        window.labels["Title"] = QLabel('Description', window)
        window.labels["Title"].setStyleSheet("color: black; font-weight: bold")
        window.labels["Title"].move(WIDTH // 2 - 110, 30)
        window.labels["Title"].setFixedSize(WIDTH - 770, 100)
        window.fonts["Title"] = window.labels["Title"].font()
        window.fonts["Title"].setPointSize(32)
        window.labels["Title"].setFont(window.fonts["Title"])

        window.labels["Description"] = QLabel(
            "Welcome to Cringe Bank! Here you can deposit money to your account," + "\n"
            "transfer it to another user and withdraw from your account." + "\n\n\n\n"
            "This app was created by Ermoshin Mikhail, 2nd year MIPT student" + "\n" +
            "as the second project for the course \"Python Programming\". If you" + "\n" +
            "find errors in the operation of this app, please report them to the mail:" + "\n" +
            "ermoshin.me@phystech.edu" + "\n\n\n" + "You can also share this project with your friends. " +
            "Enjoy it!",
            window)
        window.labels["Description"].setStyleSheet("color: black")
        window.labels["Description"].move(150, 200)
        window.labels["Description"].setFixedSize(WIDTH - 300, 300)
        window.fonts["Description"] = window.labels["Description"].font()
        window.fonts["Description"].setPointSize(16)
        window.labels["Description"].setFont(window.fonts["Description"])
        
    elif isinstance(window, windows.LogInFailInputWindow):
        window.setWindowTitle("ACCESS ERROR")
        window.setText("User name or password is wrong. Try again.")
        window.setIcon(QMessageBox.Warning)

    elif isinstance(window, windows.RegisterFailWindow):

        window.setWindowTitle("USER CREATION ERROR")
        if wrong_field == "user name":
            window.setText("This user already exists.")
        elif wrong_field == "invalid symbols":
            window.setText("Invalid user name.")
        elif wrong_field == "birthday":
            window.setText("Invalid date format entered.")
        elif wrong_field == "password":
            window.setText("The password is too short.")
        elif wrong_field == "repeat password":
            window.setText("The password is repeated incorrectly.")
        else:
            window.setText("Something went wrong. Try again.")
        window.setIcon(QMessageBox.Warning)

    elif isinstance(window, windows.RegisterSuccessWindow):

        window.setWindowTitle("SUCCESSFUL REGISTRATION")
        window.setText("Registration completed successfully. Now you can use your account.")

    elif isinstance(window, windows.AccountMainPage):

        window.labels["User name 1"] = QLabel('user name:', window)
        window.labels["User name 1"].setStyleSheet("color: black; font: italic;")
        window.labels["User name 1"].move(200, 20)
        window.labels["User name 1"].setFixedSize(140, 30)

        window.labels["User name 2"] = QLabel(windows.curr_user_name, window)
        window.labels["User name 1"].setStyleSheet("color: black; font: bold italic;")
        window.labels["User name 2"].move(380, 20)
        window.labels["User name 2"].setFixedSize(450, 30)

        window.labels["Balance 1"] = QLabel('balance:', window)
        window.labels["Balance 1"].setStyleSheet("color: black; font: italic;")
        window.labels["Balance 1"].move(200, 60)
        window.labels["Balance 1"].setFixedSize(140, 30)

        window.labels["Balance 2"] = QLabel(f"{windows.users_db.get_balance(windows.curr_user_name)} ₽", window)
        window.labels["Balance 2"].setStyleSheet("color: black; font: bold italic;")
        window.labels["Balance 2"].move(380, 60)
        window.labels["Balance 2"].setFixedSize(450, 30)

        window.fonts = defaultdict()
        for label in window.labels.keys():
            window.fonts[label] = window.labels[label].font()
            window.fonts[label].setPointSize(20)
            window.labels[label].setFont(window.fonts[label])

    elif isinstance(window, windows.SendWindow):

        window.labels["User name 1"] = QLabel('user name:', window)
        window.labels["User name 1"].setStyleSheet("color: black; font: italic;")
        window.labels["User name 1"].move(200, 20)
        window.labels["User name 1"].setFixedSize(140, 30)

        window.labels["User name 2"] = QLabel(windows.curr_user_name, window)
        window.labels["User name 1"].setStyleSheet("color: black; font: bold italic;")
        window.labels["User name 2"].move(380, 20)
        window.labels["User name 2"].setFixedSize(450, 30)

        window.labels["Balance 1"] = QLabel('balance:', window)
        window.labels["Balance 1"].setStyleSheet("color: black; font: italic;")
        window.labels["Balance 1"].move(200, 60)
        window.labels["Balance 1"].setFixedSize(140, 30)

        window.labels["Balance 2"] = QLabel(f"{windows.users_db.get_balance(windows.curr_user_name)} ₽", window)
        window.labels["Balance 2"].setStyleSheet("color: black; font: bold italic;")
        window.labels["Balance 2"].move(380, 60)
        window.labels["Balance 2"].setFixedSize(450, 30)

        window.labels["Recipient"] = QLabel('recipient: ', window)
        window.labels["Recipient"].setStyleSheet("color: black")
        window.labels["Recipient"].setFixedSize(210, 30)
        window.labels["Recipient"].move((WIDTH - 200) // 2 - 150, 298)

        window.labels["Money"] = QLabel('money to sent: ', window)
        window.labels["Money"].setStyleSheet("color: black")
        window.labels["Money"].setFixedSize(300, 30)
        window.labels["Money"].move((WIDTH - 200) // 2 - 216, 338)

        window.fonts = defaultdict()
        for label in window.labels.keys():
            window.fonts[label] = window.labels[label].font()
            window.fonts[label].setPointSize(20)
            window.labels[label].setFont(window.fonts[label])

    elif isinstance(window, windows.DepositWindow):

        window.labels["User name 1"] = QLabel('user name:', window)
        window.labels["User name 1"].setStyleSheet("color: black; font: italic;")
        window.labels["User name 1"].move(200, 20)
        window.labels["User name 1"].setFixedSize(140, 30)

        window.labels["User name 2"] = QLabel(windows.curr_user_name, window)
        window.labels["User name 1"].setStyleSheet("color: black; font: bold italic;")
        window.labels["User name 2"].move(380, 20)
        window.labels["User name 2"].setFixedSize(450, 30)

        window.labels["Balance 1"] = QLabel('balance:', window)
        window.labels["Balance 1"].setStyleSheet("color: black; font: italic;")
        window.labels["Balance 1"].move(200, 60)
        window.labels["Balance 1"].setFixedSize(140, 30)

        window.labels["Balance 2"] = QLabel(f"{windows.users_db.get_balance(windows.curr_user_name)} ₽", window)
        window.labels["Balance 2"].setStyleSheet("color: black; font: bold italic;")
        window.labels["Balance 2"].move(380, 60)
        window.labels["Balance 2"].setFixedSize(450, 30)

        window.labels["Money"] = QLabel('money to deposit: ', window)
        window.labels["Money"].setStyleSheet("color: black")
        window.labels["Money"].setFixedSize(300, 30)
        window.labels["Money"].move((WIDTH - 200) // 2 - 270, 338)

        window.fonts = defaultdict()
        for label in window.labels.keys():
            window.fonts[label] = window.labels[label].font()
            window.fonts[label].setPointSize(20)
            window.labels[label].setFont(window.fonts[label])

    elif isinstance(window, windows.WithdrawWindow):

        window.labels["User name 1"] = QLabel('user name:', window)
        window.labels["User name 1"].setStyleSheet("color: black; font: italic;")
        window.labels["User name 1"].move(200, 20)
        window.labels["User name 1"].setFixedSize(140, 30)

        window.labels["User name 2"] = QLabel(windows.curr_user_name, window)
        window.labels["User name 1"].setStyleSheet("color: black; font: bold italic;")
        window.labels["User name 2"].move(380, 20)
        window.labels["User name 2"].setFixedSize(450, 30)

        window.labels["Balance 1"] = QLabel('balance:', window)
        window.labels["Balance 1"].setStyleSheet("color: black; font: italic;")
        window.labels["Balance 1"].move(200, 60)
        window.labels["Balance 1"].setFixedSize(140, 30)

        window.labels["Balance 2"] = QLabel(f"{windows.users_db.get_balance(windows.curr_user_name)} ₽", window)
        window.labels["Balance 2"].setStyleSheet("color: black; font: bold italic;")
        window.labels["Balance 2"].move(380, 60)
        window.labels["Balance 2"].setFixedSize(450, 30)

        window.labels["Money"] = QLabel('money to withdraw: ', window)
        window.labels["Money"].setStyleSheet("color: black")
        window.labels["Money"].setFixedSize(300, 30)
        window.labels["Money"].move((WIDTH - 200) // 2 - 270, 338)

        window.fonts = defaultdict()
        for label in window.labels.keys():
            window.fonts[label] = window.labels[label].font()
            window.fonts[label].setPointSize(20)
            window.labels[label].setFont(window.fonts[label])

    elif isinstance(window, windows.OperationFailWindow):

        window.setWindowTitle("OPERATION ERROR")
        if wrong_field == "send to yourself":
            window.setText("You can't send money to yourself.")
        elif wrong_field == "recipient":
            window.setText("This recipient does not exist.")
        elif wrong_field == "money":
            window.setText("You have not enough money for operation.")
        elif wrong_field == "input":
            window.setText("incorrect input of the money field.")

        window.setIcon(QMessageBox.Warning)

    elif isinstance(window, windows.HistoryWindow):

        window.fonts = defaultdict()

        def parsed_date(date: str) -> str:
            year = date[0:4]
            month = date[5:7]
            day = date[8:10]
            hour = date[11:13]
            minute = date[14:16]
            return f"{day}.{month}.{year} {hour}:{minute}"

        operations = records_db.get_records(windows.curr_user_name)

        for i in range(len(operations)):
            date = parsed_date(str(operations[i][0]))
            operation = operations[i][1]
            value = operations[i][2]
            recipient = operations[i][3]

            operation_text = ""
            if operation == "send":
                operation_text = f"sent {value} ₽ to \"{recipient}\""
            elif operation == "withdraw":
                operation_text = f"withdrawn {value} ₽"
            elif operation == "deposit":
                operation_text = f"deposited {value} ₽"

            window.labels[f"Date {i}"] = QLabel(f"{date}:", window)
            window.labels[f"Date {i}"].setStyleSheet("color: black; font: italic;")
            window.labels[f"Date {i}"].move(60, 110 + 23 * i)
            window.labels[f"Date {i}"].setFixedSize(160, 23)

            window.labels[f"Operation {i}"] = QLabel(operation_text, window)
            window.labels[f"Operation {i}"].setStyleSheet("color: black")
            window.labels[f"Operation {i}"].move(230, 110 + 23 * i)
            window.labels[f"Operation {i}"].setFixedSize((WIDTH - 200) // 2, 23)

        window.fonts = defaultdict()
        for label in window.labels.keys():
            window.fonts[label] = window.labels[label].font()
            window.fonts[label].setPointSize(14)
            window.labels[label].setFont(window.fonts[label])

        window.labels["Title"] = QLabel("History", window)
        window.labels["Title"].setStyleSheet("color: black; font-weight: bold;")
        window.labels["Title"].move(WIDTH // 2 - 75, 30)
        window.labels["Title"].setFixedSize(WIDTH - 840, 60)
        window.fonts["Title"] = window.labels["Title"].font()
        window.fonts["Title"].setPointSize(32)
        window.labels["Title"].setFont(window.fonts["Title"])


def set_line_edits(window) -> None:

    if isinstance(window, windows.LogInWindow):

        window.line_edits["User name"] = QLineEdit(window)
        window.line_edits["User name"].setText(windows.curr_user_name)
        window.line_edits["User name"].setObjectName("user_name")
        window.line_edits["User name"].setGeometry((WIDTH - 200) // 2, 300, 400, 30)

        window.line_edits["Password"] = QLineEdit(window)
        window.line_edits["Password"].setText(windows.curr_password)
        window.line_edits["Password"].setObjectName("password")
        window.line_edits["Password"].setGeometry((WIDTH - 200) // 2, 340, 400, 30)
        window.line_edits["Password"].setEchoMode(2)

        window.fonts = defaultdict()
        for line_edit in window.line_edits.keys():
            window.fonts[line_edit] = window.line_edits[line_edit].font()
            window.fonts[line_edit].setPointSize(16)
            window.line_edits[line_edit].setFont(window.fonts[line_edit])

    elif isinstance(window, windows.RegisterWindow):

        window.line_edits["User name"] = QLineEdit(window)
        window.line_edits["User name"].setText("")
        window.line_edits["User name"].setObjectName("user_name")
        window.line_edits["User name"].setGeometry((WIDTH - 200) // 2, 300, 400, 30)

        window.line_edits["Birthday"] = QLineEdit(window)
        window.line_edits["Birthday"].setText("")
        window.line_edits["Birthday"].setObjectName("birthday")
        window.line_edits["Birthday"].setGeometry((WIDTH - 200) // 2, 338, 400, 30)

        window.line_edits["Password"] = QLineEdit(window)
        window.line_edits["Password"].setText("")
        window.line_edits["Password"].setObjectName("password")
        window.line_edits["Password"].setGeometry((WIDTH - 200) // 2, 378, 400, 30)
        window.line_edits["Password"].setEchoMode(2)

        window.line_edits["Repeat password"] = QLineEdit(window)
        window.line_edits["Repeat password"].setText("")
        window.line_edits["Repeat password"].setObjectName("repeat_password")
        window.line_edits["Repeat password"].setGeometry((WIDTH - 200) // 2, 418, 400, 30)
        window.line_edits["Repeat password"].setEchoMode(2)

        window.fonts = defaultdict()
        for line_edit in window.line_edits.keys():
            window.fonts[line_edit] = window.line_edits[line_edit].font()
            window.fonts[line_edit].setPointSize(16)
            window.line_edits[line_edit].setFont(window.fonts[line_edit])

    elif isinstance(window, windows.SendWindow):

        window.line_edits["Recipient"] = QLineEdit(window)
        window.line_edits["Recipient"].setText("")
        window.line_edits["Recipient"].setObjectName("recipient")
        window.line_edits["Recipient"].setGeometry((WIDTH - 200) // 2, 298, 400, 30)

        window.line_edits["Money"] = QLineEdit(window)
        window.line_edits["Money"].setText("")
        window.line_edits["Money"].setObjectName("money")
        window.line_edits["Money"].setGeometry((WIDTH - 200) // 2, 338, 400, 30)

        window.fonts = defaultdict()
        for line_edit in window.line_edits.keys():
            window.fonts[line_edit] = window.line_edits[line_edit].font()
            window.fonts[line_edit].setPointSize(16)
            window.line_edits[line_edit].setFont(window.fonts[line_edit])

    elif isinstance(window, windows.DepositWindow):

        window.line_edits["Money"] = QLineEdit(window)
        window.line_edits["Money"].setText("")
        window.line_edits["Money"].setObjectName("money")
        window.line_edits["Money"].setGeometry((WIDTH - 200) // 2, 338, 400, 30)

        window.fonts = defaultdict()
        for line_edit in window.line_edits.keys():
            window.fonts[line_edit] = window.line_edits[line_edit].font()
            window.fonts[line_edit].setPointSize(16)
            window.line_edits[line_edit].setFont(window.fonts[line_edit])

    elif isinstance(window, windows.WithdrawWindow):

        window.line_edits["Money"] = QLineEdit(window)
        window.line_edits["Money"].setText("")
        window.line_edits["Money"].setObjectName("money")
        window.line_edits["Money"].setGeometry((WIDTH - 200) // 2, 338, 400, 30)

        window.fonts = defaultdict()
        for line_edit in window.line_edits.keys():
            window.fonts[line_edit] = window.line_edits[line_edit].font()
            window.fonts[line_edit].setPointSize(16)
            window.line_edits[line_edit].setFont(window.fonts[line_edit])


def goto(window, new_window, close: bool) -> None:
    if close:
        window.close()
    window.new_window = new_window
    window.new_window.show()
