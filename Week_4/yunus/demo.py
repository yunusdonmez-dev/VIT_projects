
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout # Only what I need
from PyQt6.QtGui import QIcon # Fot the icon of the programma

class My_App(QWidget):  # New class is made that inherit from QWidget
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Hello app')  # These are methode of QWidget class
        self.setWindowIcon(QIcon('check_icon.png'))
        self.resize(500, 350)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Widgets
        self.inputField = QLineEdit()
        button = QPushButton('&Say Hello')
        button.clicked.connect(self.sayHello)
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)
        
    def sayHello(self):
        inputText = self.inputField.text()
        self.output.setText('Hello {0}'.format(inputText))


app = QApplication(sys.argv) #
app.setStyleSheet('''
    QWidget {
        font-size: 25px;                 
    }
    QPushButton {
        font-size: 20px;                 
    }
                  
''')

window = My_App()
window.show()
sys.exit(app.exec())

