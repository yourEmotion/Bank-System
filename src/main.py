import sys

from PyQt5.QtWidgets import QApplication

from windows import MainMenu

from Database.users import UsersDB
from Database.records import RecordsDB


def launch_app():
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    launch_app()

