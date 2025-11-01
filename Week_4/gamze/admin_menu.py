# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)

        # Ana layout
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(15)

        # Header Frame
        self.frame_header = QtWidgets.QFrame(Dialog)
        self.frame_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setMinimumHeight(120)

        # Header iç layout
        self.header_layout = QtWidgets.QHBoxLayout(self.frame_header)
        self.header_layout.setContentsMargins(20, 10, 20, 10)
        self.header_layout.setSpacing(50)

        # Logo ve başlık frame
        self.frame_logo_title = QtWidgets.QFrame(self.frame_header)
        layout_logo_title = QtWidgets.QHBoxLayout(self.frame_logo_title)
        layout_logo_title.setContentsMargins(0, 0, 0, 0)
        layout_logo_title.setSpacing(30)  # logo ve başlık arası boşluk

        # Logo
        self.label_logo = QtWidgets.QLabel(self.frame_logo_title)
        pixmap = QtGui.QPixmap("/Users/pinhanderler/Downloads/logo.png")
        self.label_logo.setPixmap(pixmap)
        self.label_logo.setScaledContents(True)
        self.label_logo.setFixedSize(120, 80)
        layout_logo_title.addWidget(self.label_logo, alignment=QtCore.Qt.AlignVCenter)

        # Başlık
        self.label_title = QtWidgets.QLabel("ADMIN MENU", self.frame_logo_title)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        layout_logo_title.addWidget(self.label_title, alignment=QtCore.Qt.AlignVCenter)

        # Solda ortala
        self.header_layout.addWidget(self.frame_logo_title, alignment=QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        # Sağdaki butonlar
        self.frame_content = QtWidgets.QFrame(self.frame_header)
        self.frame_content.setMaximumWidth(320)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_2.setContentsMargins(5, 10, 5, 10)
        self.verticalLayout_2.setSpacing(12)

        # Butonlar
        self.pushButton_settings = QtWidgets.QPushButton("PREFERENCES - ADMIN")
        self.pushButton_exit = QtWidgets.QPushButton("EXIT")
        self.pushButton_event = QtWidgets.QPushButton("EVENT CONTROL")
        self.pushButton_mail = QtWidgets.QPushButton("SEND MAIL")

        button_style = """
        QPushButton{
            background-color: rgb(255, 255, 255);
            border-radius: 10px;
            border: 2px solid rgb(171, 171, 171);
            font-size: 14px;
            font-weight: bold;
            min-height: 40px;
        }
        QPushButton:hover {
            background-color: rgb(255, 226, 229);
        }
        QPushButton:pressed {
            background-color: rgb(218, 30, 60);
            color: rgb(255, 255, 255);
        }
        """

        for btn in [self.pushButton_settings, self.pushButton_exit,
                    self.pushButton_event, self.pushButton_mail]:
            btn.setStyleSheet(button_style)
            self.verticalLayout_2.addWidget(btn)

        self.header_layout.addWidget(self.frame_content, alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # Header'ı ekle
        self.verticalLayout.addWidget(self.frame_header)

        # Spacer
        self.verticalLayout.addSpacing(10)

        # Table
        self.table_events = QtWidgets.QTableWidget(Dialog)
        self.table_events.setColumnCount(4)
        self.table_events.setRowCount(0)
        self.table_events.setHorizontalHeaderLabels(
            ["EVENT NAME", "START TIME", "PARTICIPANT E-MAIL", "ORGANIZER E-MAIL"]
        )
        self.table_events.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_events.setStyleSheet("""
        QTableWidget {
            background-color: #2a2d33;
            color: white;
            gridline-color: #444;
            selection-background-color: #50555e;
        }
        QHeaderView::section {
            background-color: #3c414a;
            color: white;
            padding: 4px;
            border: 1px solid #444;
        }
        """)
        self.verticalLayout.addWidget(self.table_events)

        # Buton eventleri
        self.pushButton_exit.clicked.connect(Dialog.close)
        self.pushButton_settings.clicked.connect(lambda: print("Preferences clicked"))
        self.pushButton_event.clicked.connect(lambda: print("Event Control clicked"))
        self.pushButton_mail.clicked.connect(lambda: print("Send Mail clicked"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())