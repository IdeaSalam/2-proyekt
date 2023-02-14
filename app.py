from data.main import Mainwindow
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication
import sys
if __name__=='__main__':
    app = QApplication(sys.argv)
    win = Mainwindow(1000,500, "My_project")
    style = """
    background-image:url("image//bulut.jpg");
    """
    win.setStyleSheet(style)
    win.show()
    app.exec()
    
