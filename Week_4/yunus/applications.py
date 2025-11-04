from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QMainWindow # Only what I need
from PyQt6.QtGui import QIcon # Fot the icon of the programma
from PyQt6 import uic
import sys

class My_App(QMainWindow):  # New class is made that inherit from QWidget
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('Week_4/yunus/applications.ui', self)  # type: ignore
        self.setWindowTitle('Application Page')  # These are methode of QWidget class
        self.setWindowIcon(QIcon('Week_4/yunus/check_icon.png'))
        self.back_button.clicked.connect(self.menu_page) # type: ignore

    def menu_page(self):
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