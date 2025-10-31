from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QMainWindow # Only what I need
from PyQt6.QtGui import QIcon # For the icon of the programma
from PyQt6 import uic
import sys

class My_App(QMainWindow):  # New class is made that inherit from QWidget
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('yunus/login.ui', self)  # type: ignore
        self.setWindowTitle('Login Page')  # These are methode of QWidget class
        self.setWindowIcon(QIcon('yunus/check_icon.png'))
        self.login_button.clicked.connect(self.login) # type: ignore

    def login(self):
        from menu import MainWindow
        self.main = MainWindow()
        self.main.show()
        self.close()
        
if __name__ == '__main__':

    app = QApplication(sys.argv)

    my_app = My_App()
    my_app.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing window...')