from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox

from collections import defaultdict
from string import ascii_letters, digits

from src.Windows.TextStyles import day_mode_styles as day
from src.Windows.TextStyles import night_mode_styles as night

import src.Windows.window_functools as wf

from src.Database.users import users_db
from src.Database.records import records_db

NIGHT_MODE_ON = False

curr_user_name = ""
curr_password = ""
first_usage = False


class MainMenu(QMainWindow):
    buttons = defaultdict()
    labels = defaultdict()
    line_edits = defaultdict()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRINGE BANK")
        self.setFixedWidth(wf.WIDTH)
        self.setFixedHeight(wf.HEIGHT)
        wf.move_to_center(self)

        wf.set_buttons(self)
        wf.set_labels(self)
        wf.set_line_edits(self)

        if NIGHT_MODE_ON:
            night.set_style_sheets(self)
        else:
            day.set_style_sheets(self)

    def switch_night_mode(self):
        global NIGHT_MODE_ON
        if NIGHT_MODE_ON:
            NIGHT_MODE_ON = False
            day.set_style_sheets(self)
        else:
            NIGHT_MODE_ON = True
            night.set_style_sheets(self)

    def register_button_press(self):
        wf.goto(window=self,
                new_window=RegisterWindow(),
                close=True)

    def log_in_button_press(self):
        wf.goto(window=self,
                new_window=LogInWindow(),
                close=True)

    def description_button_press(self):
        wf.goto(window=self,
                new_window=DescriptionWindow(),
                close=True)


class LogInWindow(QWidget):
    buttons = defaultdict()
    labels = defaultdict()
    line_edits = defaultdict()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRINGE BANK")
        self.setFixedWidth(wf.WIDTH)
        self.setFixedHeight(wf.HEIGHT)
        wf.move_to_center(self)

        self.curr_user_name = ""
        self.curr_password = ""

        wf.set_buttons(self)
        wf.set_labels(self)
        wf.set_line_edits(self)

        if NIGHT_MODE_ON:
            night.set_style_sheets(self)
        else:
            day.set_style_sheets(self)

    def switch_night_mode(self):
        global NIGHT_MODE_ON

        if NIGHT_MODE_ON:
            NIGHT_MODE_ON = False
            day.set_style_sheets(self)
        else:
            NIGHT_MODE_ON = True
            night.set_style_sheets(self)

    def back_button_press(self):
        wf.goto(window=self,
                new_window=MainMenu(),
                close=True)

    def log_in_button_press(self):
        self.curr_user_name = self.line_edits["User name"].text()
        self.curr_password = self.line_edits["Password"].text()

        if users_db.in_database(self.curr_user_name, self.curr_password):
            global curr_user_name, curr_password
            curr_user_name = self.curr_user_name
            curr_password = self.curr_password

            wf.goto(window=self,
                    new_window=AccountMainPage(),
                    close=True)
        else:
            wf.goto(window=self,
                    new_window=LogInFailInputWindow(),
                    close=False)


class RegisterWindow(QWidget):
    buttons = defaultdict()
    labels = defaultdict()
    line_edits = defaultdict()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRINGE BANK")
        self.setFixedWidth(wf.WIDTH)
        self.setFixedHeight(wf.HEIGHT)
        wf.move_to_center(self)

        self.curr_user_name = ""
        self.curr_birthday = ""
        self.curr_password = ""
        self.curr_repeat_password = ""

        wf.set_buttons(self)
        wf.set_labels(self)
        wf.set_line_edits(self)

        if NIGHT_MODE_ON:
            night.set_style_sheets(self)
        else:
            day.set_style_sheets(self)

    def switch_night_mode(self):
        global NIGHT_MODE_ON
        if NIGHT_MODE_ON:
            NIGHT_MODE_ON = False
            day.set_style_sheets(self)
        else:
            NIGHT_MODE_ON = True
            night.set_style_sheets(self)

    def back_button_press(self):
        wf.goto(window=self,
                new_window=MainMenu(),
                close=True)

    def register_button_press(self):
        self.curr_user_name = self.line_edits["User name"].text()
        self.curr_birthday = self.line_edits["Birthday"].text()
        self.curr_password = self.line_edits["Password"].text()
        self.curr_repeat_password = self.line_edits["Repeat password"].text()

        def date_is_correct(date: str) -> bool:
            import datetime

            try:
                year = int(date[6:10])
                month = int(date[3:5])
                _day = int(date[0:2])
                if date[2] != "." or date[5] != ".":
                    return False
                datetime.date(year, month, _day)
                return True
            except:
                return False

        def parse_date(date: str) -> str:
            year = date[6:10]
            month = date[3:5]
            _day = date[0:2]
            return f"{year}-{month}-{_day}"

        def valid_user_name(name: str) -> bool:
            valid_symbols = set(ascii_letters + digits + "_")
            for symbol in name:
                if symbol not in valid_symbols:
                    return False
            return True

        if not valid_user_name(self.curr_user_name) or len(self.curr_user_name) < 3:
            wf.goto(window=self,
                    new_window=RegisterFailWindow(wrong_field="invalid symbols"),
                    close=False)

        elif users_db.in_database(self.curr_user_name):
            wf.goto(window=self,
                    new_window=RegisterFailWindow(wrong_field="user name"),
                    close=False)

        elif len(self.curr_password) < 6:
            wf.goto(window=self,
                    new_window=RegisterFailWindow(wrong_field="password"),
                    close=False)

        elif self.curr_password != self.curr_repeat_password:
            wf.goto(window=self,
                    new_window=RegisterFailWindow(wrong_field="repeat password"),
                    close=False)

        elif not date_is_correct(self.curr_birthday):
            wf.goto(window=self,
                    new_window=RegisterFailWindow(wrong_field="birthday"),
                    close=False)

        else:
            self.curr_birthday = parse_date(self.curr_birthday)
            users_db.insert(self.curr_user_name, self.curr_password, self.curr_birthday)

            global curr_user_name, curr_password, first_usage
            curr_user_name = self.curr_user_name
            curr_password = self.curr_password
            first_usage = True

            wf.goto(window=self,
                    new_window=AccountMainPage(),
                    close=True)


class DescriptionWindow(QWidget):
    buttons = defaultdict()
    labels = defaultdict()
    line_edits = defaultdict()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRINGE BANK")
        self.setFixedWidth(wf.WIDTH)
        self.setFixedHeight(wf.HEIGHT)
        wf.move_to_center(self)

        wf.set_buttons(self)
        wf.set_labels(self)
        wf.set_line_edits(self)

        if NIGHT_MODE_ON:
            night.set_style_sheets(self)
        else:
            day.set_style_sheets(self)

    def switch_night_mode(self):
        global NIGHT_MODE_ON

        if NIGHT_MODE_ON:
            NIGHT_MODE_ON = False
            day.set_style_sheets(self)
        else:
            NIGHT_MODE_ON = True
            night.set_style_sheets(self)

    def back_button_press(self):
        wf.goto(window=self,
                new_window=MainMenu(),
                close=True)


class LogInFailInputWindow(QMessageBox):
    labels = defaultdict()

    def __init__(self):
        super().__init__()

        wf.set_labels(self)


class RegisterFailWindow(QMessageBox):
    labels = defaultdict()

    def __init__(self, wrong_field):
        super().__init__()

        wf.set_labels(self, wrong_field)


class RegisterSuccessWindow(QMessageBox):
    labels = defaultdict()

    def __init__(self):
        super().__init__()

        wf.set_labels(self)


class AccountMainPage(QMainWindow):
    buttons = defaultdict()
    labels = defaultdict()
    line_edits = defaultdict()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRINGE BANK")
        self.setFixedWidth(wf.WIDTH)
        self.setFixedHeight(wf.HEIGHT)
        wf.move_to_center(self)

        wf.set_buttons(self)
        wf.set_labels(self)

        if NIGHT_MODE_ON:
            night.set_style_sheets(self)
        else:
            day.set_style_sheets(self)

        global first_usage
        if first_usage:
            wf.goto(window=self,
                    new_window=RegisterSuccessWindow(),
                    close=False)
            first_usage = False

    def send_button_press(self):
        wf.goto(window=self,
                new_window=SendWindow(),
                close=True)

    def withdraw_button_press(self):
        wf.goto(window=self,
                new_window=WithdrawWindow(),
                close=True)

    def deposit_button_press(self):
        wf.goto(window=self,
                new_window=DepositWindow(),
                close=True)

    def view_history_button_press(self):
        wf.goto(window=self,
                new_window=HistoryWindow(),
                close=True)

    def switch_night_mode(self):
        global NIGHT_MODE_ON

        if NIGHT_MODE_ON:
            NIGHT_MODE_ON = False
            day.set_style_sheets(self)
        else:
            NIGHT_MODE_ON = True
            night.set_style_sheets(self)

    def back_button_press(self):
        wf.goto(window=self,
                new_window=MainMenu(),
                close=True)


class SendWindow(QWidget):
    buttons = defaultdict()
    labels = defaultdict()
    line_edits = defaultdict()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRINGE BANK")
        self.setFixedWidth(wf.WIDTH)
        self.setFixedHeight(wf.HEIGHT)
        wf.move_to_center(self)

        wf.set_buttons(self)
        wf.set_labels(self)
        wf.set_line_edits(self)

        if NIGHT_MODE_ON:
            night.set_style_sheets(self)
        else:
            day.set_style_sheets(self)

    def confirm_button_press(self):
        old_balance = users_db.get_balance(curr_user_name)

        try:
            money_sent = int(self.line_edits["Money"].text())
            if money_sent < 0:
                raise Exception

        except:
            wf.goto(window=self,
                    new_window=OperationFailWindow(wrong_field="input"),
                    close=False)
            return

        recipient = self.line_edits["Recipient"].text()

        if not users_db.in_database(recipient):
            wf.goto(window=self,
                    new_window=OperationFailWindow(wrong_field="recipient"),
                    close=False)

        elif old_balance < money_sent:
            wf.goto(window=self,
                    new_window=OperationFailWindow(wrong_field="money"),
                    close=False)

        else:
            records_db.insert(curr_user_name, "send", money_sent, recipient)
            users_db.update_balance(curr_user_name, old_balance - money_sent)
            users_db.update_balance(recipient, old_balance + money_sent)

            wf.goto(window=self,
                    new_window=OperationSuccessWindow(self),
                    close=False)

    def back_button_press(self):
        wf.goto(window=self,
                new_window=AccountMainPage(),
                close=True)

    def switch_night_mode(self):
        global NIGHT_MODE_ON

        if NIGHT_MODE_ON:
            NIGHT_MODE_ON = False
            day.set_style_sheets(self)
        else:
            NIGHT_MODE_ON = True
            night.set_style_sheets(self)


class WithdrawWindow(QWidget):
    buttons = defaultdict()
    labels = defaultdict()
    line_edits = defaultdict()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRINGE BANK")
        self.setFixedWidth(wf.WIDTH)
        self.setFixedHeight(wf.HEIGHT)
        wf.move_to_center(self)

        wf.set_buttons(self)
        wf.set_labels(self)
        wf.set_line_edits(self)

        if NIGHT_MODE_ON:
            night.set_style_sheets(self)
        else:
            day.set_style_sheets(self)

    def confirm_button_press(self):
        old_balance = users_db.get_balance(curr_user_name)

        try:
            money_withdrawn = int(self.line_edits["Money"].text())
            if money_withdrawn < 0:
                raise Exception

        except:
            wf.goto(window=self,
                    new_window=OperationFailWindow(wrong_field="input"),
                    close=False)
            return

        if old_balance < money_withdrawn:
            wf.goto(window=self,
                    new_window=OperationFailWindow(wrong_field="money"),
                    close=False)

        else:
            records_db.insert(curr_user_name, "withdraw", money_withdrawn)
            users_db.update_balance(curr_user_name, old_balance - money_withdrawn)

            wf.goto(window=self,
                    new_window=OperationSuccessWindow(self),
                    close=False)

    def back_button_press(self):
        wf.goto(window=self,
                new_window=AccountMainPage(),
                close=True)

    def switch_night_mode(self):
        global NIGHT_MODE_ON

        if NIGHT_MODE_ON:
            NIGHT_MODE_ON = False
            day.set_style_sheets(self)
        else:
            NIGHT_MODE_ON = True
            night.set_style_sheets(self)


class DepositWindow(QWidget):
    buttons = defaultdict()
    labels = defaultdict()
    line_edits = defaultdict()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRINGE BANK")
        self.setFixedWidth(wf.WIDTH)
        self.setFixedHeight(wf.HEIGHT)
        wf.move_to_center(self)

        wf.set_buttons(self)
        wf.set_labels(self)
        wf.set_line_edits(self)

        if NIGHT_MODE_ON:
            night.set_style_sheets(self)
        else:
            day.set_style_sheets(self)

    def confirm_button_press(self):
        old_balance = users_db.get_balance(curr_user_name)

        try:
            money_deposited = int(self.line_edits["Money"].text())
            if money_deposited < 0:
                print(money_deposited)
                raise Exception

        except:
            wf.goto(window=self,
                    new_window=OperationFailWindow(wrong_field="input"),
                    close=False)
            return

        records_db.insert(curr_user_name, "deposit", money_deposited)
        users_db.update_balance(curr_user_name, old_balance + money_deposited)

        wf.goto(window=self,
                new_window=OperationSuccessWindow(self),
                close=False)

    def back_button_press(self):
        wf.goto(window=self,
                new_window=AccountMainPage(),
                close=True)

    def switch_night_mode(self):
        global NIGHT_MODE_ON

        if NIGHT_MODE_ON:
            NIGHT_MODE_ON = False
            day.set_style_sheets(self)
        else:
            NIGHT_MODE_ON = True
            night.set_style_sheets(self)


class HistoryWindow(QWidget):
    buttons = defaultdict()
    labels = defaultdict()
    line_edits = defaultdict()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRINGE BANK")
        self.setFixedWidth(wf.WIDTH)
        self.setFixedHeight(wf.HEIGHT)
        wf.move_to_center(self)

        wf.set_buttons(self)
        wf.set_labels(self)
        wf.set_line_edits(self)

        if NIGHT_MODE_ON:
            night.set_style_sheets(self)
        else:
            day.set_style_sheets(self)

    def back_button_press(self):
        wf.goto(window=self,
                new_window=AccountMainPage(),
                close=True)

    def switch_night_mode(self):
        global NIGHT_MODE_ON

        if NIGHT_MODE_ON:
            NIGHT_MODE_ON = False
            day.set_style_sheets(self)
        else:
            NIGHT_MODE_ON = True
            night.set_style_sheets(self)


class OperationSuccessWindow(QMessageBox):
    def __init__(self, window):
        super().__init__()
        self.prev_window = window
        self.setWindowTitle("SUCCESSFUL OPERATION")
        self.setText("Operation completed successfully.")

        wf.set_buttons(self)

    def closeEvent(self, event):
        self.prev_window.close()
        wf.goto(window=self,
                new_window=AccountMainPage(),
                close=True)

    def ok_button_press(self):
        self.prev_window.close()
        wf.goto(window=self,
                new_window=AccountMainPage(),
                close=True)


class OperationFailWindow(QMessageBox):
    def __init__(self, wrong_field):
        super().__init__()
        self.setFixedWidth(wf.WIDTH)
        self.setFixedHeight(wf.HEIGHT)
        wf.move_to_center(self)

        wf.set_labels(self, wrong_field)
