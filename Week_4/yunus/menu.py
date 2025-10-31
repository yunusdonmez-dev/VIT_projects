from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QMainWindow # Only what I need
from PyQt6.QtGui import QIcon # Fot the icon of the programma
from PyQt6 import uic
import sys

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('yunus/menu.ui', self)  # type: ignore
        self.setWindowTitle('Menu Page')  # These are methode of QWidget class
        self.setWindowIcon(QIcon('yunus/check_icon.png'))
        self.log_out_button.clicked.connect(self.login_page)  # type: ignore
        self.app_button.clicked.connect(self.application_page)  # type: ignore
        
    def login_page(self):
        from login import LoginPage
        self.main = LoginPage()
        self.main.show()
        self.close()

    def application_page(self):
        from applications import My_App
        self.main = My_App()
        self.main.show()
        self.close()
        
if __name__ == '__main__':

    app = QApplication(sys.argv)

    my_app = MainWindow()
    my_app.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing window...')