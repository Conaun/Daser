# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\工作\ImproveEff\DeploymentPrepared\deploy_prepared.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from generateFile import generateFile


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(835, 679)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.openFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFileButton.setObjectName("openFileButton")
        self.horizontalLayout_2.addWidget(self.openFileButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.openFileButton, self.lineEdit)
        
        # 初始化，完善功能
        self.errorMsg = str()
        self.open_file_path = str() 
        self.file_path_list = list()
        self.count = 0

        tmp_str = ('=' * 70 + '\ndata.txt文件格式说明\n' + '=' * 70
                    + '\n[工程中的相对路径]\n'
                    + '如:\n'
                    + 'src/yfjz/com/nipsoft/nipis/yfjz/batchvaccine/action/AddBatchVaccineAction.java')
        self.textBrowser.setText(tmp_str)

        # 绑定事件
        self.openFileButton.clicked.connect(self.open_dirth_path_func)
        self.startButton.clicked.connect(self.start_func)

    '''
    执行主主程序
    '''
    def start_func(self):
        for file_path in self.file_path_list:
            msg = generateFile(file_path)
            self.count += 1
            self.textBrowser.append("{}. {}".format(self.count, msg))
        self.count = 0
        self.textBrowser.append('执行结束！\n')

    '''
    展示配置文件中的信息,并保存
    '''
    def list_info(self):
        try:
            data_file = open(self.open_file_path, 'r', encoding='utf-8')
            self.file_path_list.clear()
            for line in data_file:
                self.file_path_list.append(line)
            self.textBrowser.append('需要准备文件的个数: ' + str(len(self.file_path_list)) + '\n')
        except Exception as e:
            self.errorMsg = str(e)
            self.textBrowser.append(self.errorMsg + '\n')
    '''
    打开文件夹——Button
    '''
    def open_dirth_path_func(self):
        self.open_file_path, _= QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', './*.csv')
        if self.open_file_path != '':
            self.lineEdit.setText(self.open_file_path)
            self.list_info() # 展示配置文件中的信息

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openFileButton.setText(_translate("MainWindow", "打开文件"))
        self.startButton.setText(_translate("MainWindow", "开始"))
