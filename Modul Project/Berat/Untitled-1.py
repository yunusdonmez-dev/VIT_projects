import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import os

users = [
    {"kullanici": "ahmet", "parola": "werhere", "yetki": "admin"},
    {"kullanici": "mehmet", "parola": "itforever", "yetki": "user"},
    {"kullanici": "selim", "parola": "cyber_warrior", "yetki": "user"},
    {"kullanici": "ayse", "parola": "b1love", "yetki": "admin"},
    {"kullanici": "suleyman", "parola": "D_34", "yetki": "user"},
    {"kullanici": "123", "parola": "123", "yetki": "admin"},
    {"kullanici": "asd", "parola": "asd", "yetki": "user"}

]
current_dir = os.getcwd()
login_ui_path = os.path.join(current_dir, "User Interfaces", "login.ui")
admin_ui_path = os.path.join(current_dir, "User Interfaces", "admin_main.ui")
mentor_ui_path = os.path.join(current_dir, "User Interfaces", "mentor.ui")
app_ui_path = os.path.join(current_dir, "User Interfaces", "applications.ui")
int_ui_path = os.path.join(current_dir, "User Interfaces", "interviews.ui")
pref_ui_path = os.path.join(current_dir, "User Interfaces", "preferences.ui")
admin_menu_ui_path = os.path.join(current_dir, "User Interfaces", "admin_menu.ui")

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(login_ui_path, self)
        self.button_login.clicked.connect(self.login)
        self.button_exit.clicked.connect(self.exit)
        
    def exit(self):
        self.close()

    def login(self):
        username = self.Username.text()
        password = self.Password.text()
        for u in users:
            if u["kullanici"] == username and u["parola"] == password:
                if u["yetki"]== "admin":
                    self.admin_window = AdminMain() 
                    self.admin_window.show()        
                    self.close()
                else:
                    self.admin_menu_window = Prefs() 
                    self.admin_menu_window.show()        
                    self.close()
            else:
                self.error.setText("Incorrect Username or Password!")


class Prefs(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(pref_ui_path, self)
        self.button_mentor.clicked.connect(self.open_mentor)
        self.button_exit.clicked.connect(self.exit)
        self.button_app.clicked.connect(self.open_app)
        self.button_int.clicked.connect(self.open_interviews)
        self.button_main.clicked.connect(self.open_login)

    def open_login(self):
        self.login_window = LoginWindow() 
        self.login_window.show()        
        self.close()

    def open_app(self):
        self.app_window = Applications() 
        self.app_window.show()        
        self.close()

    def open_interviews(self):
        self.int_window = Interviews() 
        self.int_window.show()        
        self.close()

    def open_mentor(self):
        self.mentor_window = Mentor() 
        self.mentor_window.show()        
        self.close()

    def exit(self):
        self.close()

class AdminMain(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(admin_ui_path, self)
        self.button_mentor.clicked.connect(self.open_mentor)
        self.button_exit.clicked.connect(self.exit)
        self.button_app.clicked.connect(self.open_app)
        self.button_int.clicked.connect(self.open_interviews)
        self.button_admin.clicked.connect(self.open_admin_menu)
        self.button_main.clicked.connect(self.open_login)

    def open_login(self):
        self.login_window = LoginWindow() 
        self.login_window.show()        
        self.close()

    def open_app(self):
        self.app_window = Applications() 
        self.app_window.show()        
        self.close()

    def open_interviews(self):
        self.int_window = Interviews() 
        self.int_window.show()        
        self.close()
    
    def open_admin_menu(self):
        self.admin_menu_window = AdminMenu() 
        self.admin_menu_window.show()        
        self.close()

    def open_mentor(self):
        self.mentor_window = Mentor() 
        self.mentor_window.show()        
        self.close()

    def exit(self):
        self.close()


class Mentor(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(mentor_ui_path, self)
        self.button_back.clicked.connect(self.open_admin)
        self.button_exit.clicked.connect(self.exit)

    def open_admin(self):
        self.admin_window = AdminMain() 
        self.admin_window.show()        
        self.close()

    def exit(self):
        self.close()

class AdminMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(admin_menu_ui_path, self)
        self.button_back.clicked.connect(self.open_admin)
        self.button_exit.clicked.connect(self.exit)

    def open_admin(self):
        self.admin_window = AdminMain() 
        self.admin_window.show()        
        self.close()

    def exit(self):
        self.close()

class Interviews(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(int_ui_path, self)
        self.button_back.clicked.connect(self.open_admin)
        self.button_exit.clicked.connect(self.exit)

    def open_admin(self):
        self.admin_window = AdminMain() 
        self.admin_window.show()        
        self.close()

    def exit(self):
        self.close()

class Applications(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(app_ui_path, self)
        self.button_back.clicked.connect(self.open_admin)
        self.button_exit.clicked.connect(self.exit)

    def open_admin(self):
        self.admin_window = AdminMain() 
        self.admin_window.show()        
        self.close()

    def exit(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())