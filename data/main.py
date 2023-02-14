from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon
from data.get_weather import get_weather
class Mainwindow(QMainWindow):
    def __init__(self, width = 800, height = 220, tytle = "Qt") -> None:
        super().__init__()
        self.setWindowTitle(tytle)
        self.setGeometry(500, 200, width, height)
        icon_tytle = QIcon("image\icon_title.png")
        far_icon = QIcon("image//f.png")
        self.setWindowIcon(icon_tytle)
        self.fbutton = QPushButton(far_icon," Farg'ona",self)
        self.fbutton.setGeometry(width//2-480, 20, 150, 50)
        self.fbutton.setIcon(QIcon())
        self.temp1 = QLabel("Harorat ",self)
        self.temp1.setGeometry(width//2-460, 70, 150, 50)
        self.tbutton = QPushButton(far_icon," Toshkent",self)
        self.tbutton.setGeometry(width//2-880, 20, 150, 50)
        self.temp2 = QLabel("Harorat ",self)
        self.temp2.setGeometry(width//2-860, 70, 150, 50)
        self.fbutton.clicked.connect(self.get_weather)
        self.tbutton.clicked.connect(self.get_weather2)
        self.fbutton.setStyleSheet("QPushButton { background-color: yellow}")
        
    def get_weather(self):
        temp1 = get_weather(city="фергана")
        self.temp1.setText("Harorat: "+temp1)
    def get_weather2(self):
        temp2 = get_weather(city="фергана")
        self.temp2.setText("Harorat: "+temp2)
        
        