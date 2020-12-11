import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_deploy_prepared import *
from Daser_dialog import *

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    version_dialog = Daser_dialog()
    myWin.actionversion.triggered.connect(version_dialog.OPEN)
    sys.exit(app.exec_())