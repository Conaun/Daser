import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_version_dialog import *

class Daser_dialog(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(Daser_dialog, self).__init__(parent)
        self.setupUi(self)