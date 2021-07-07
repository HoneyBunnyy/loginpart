import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.sign_up import *


class sign_up_Window(QMainWindow, Ui_sign_up):
    def __init__(self, parent=None):
        super(sign_up_Window, self).__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = sign_up_Window()
    myWin.show()
    sys.exit(app.exec_())