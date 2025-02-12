# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ImageLabel import ImageLabel
from ListBox import ListBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1373, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.LabelImage = QtWidgets.QLabel(self.centralwidget)
        self.LabelImage = ImageLabel(self.centralwidget)
        self.LabelImage.setGeometry(QtCore.QRect(240, 50, 820, 500))
        self.LabelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelImage.setObjectName("LabelImage")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(1070, 60, 281, 481))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.EtLabel = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.EtLabel.setObjectName("EtLabel")
        self.gridLayout.addWidget(self.EtLabel, 11, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.PtnNext = QtWidgets.QPushButton(self.formLayoutWidget)
        self.PtnNext.setObjectName("PtnNext")
        self.gridLayout.addWidget(self.PtnNext, 7, 2, 1, 1)
        self.EditMode = QtWidgets.QPushButton(self.formLayoutWidget)
        self.EditMode.setObjectName("EditMode")
        self.gridLayout.addWidget(self.EditMode, 0, 2, 1, 1)
        self.EtBRcoor = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.EtBRcoor.setObjectName("EtBRcoor")
        self.gridLayout.addWidget(self.EtBRcoor, 5, 2, 1, 1)
        self.EtTRcoor = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.EtTRcoor.setObjectName("EtTRcoor")
        self.gridLayout.addWidget(self.EtTRcoor, 2, 2, 1, 1)
        self.BtnStart = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BtnStart.setObjectName("BtnStart")
        self.gridLayout.addWidget(self.BtnStart, 0, 0, 1, 1)
        self.Labelcoor = QtWidgets.QLabel(self.formLayoutWidget)
        self.Labelcoor.setObjectName("Labelcoor")
        self.gridLayout.addWidget(self.Labelcoor, 1, 0, 1, 1)
        self.EtBLcoor = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.EtBLcoor.setEnabled(True)
        self.EtBLcoor.setObjectName("EtBLcoor")
        self.gridLayout.addWidget(self.EtBLcoor, 5, 0, 1, 1)
        self.BtnPre = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BtnPre.setObjectName("BtnPre")
        self.gridLayout.addWidget(self.BtnPre, 7, 0, 1, 1)
        self.BtnRec = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BtnRec.setObjectName("BtnRec")
        self.gridLayout.addWidget(self.BtnRec, 8, 0, 1, 1)
        self.BtnSave = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BtnSave.setObjectName("BtnSave")
        self.gridLayout.addWidget(self.BtnSave, 8, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.EtTLcoor = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EtTLcoor.sizePolicy().hasHeightForWidth())
        self.EtTLcoor.setSizePolicy(sizePolicy)
        self.EtTLcoor.setObjectName("EtTLcoor")
        self.gridLayout.addWidget(self.EtTLcoor, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 9, 2, 1, 1)
        self.Labellabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.Labellabel.setObjectName("Labellabel")
        self.gridLayout.addWidget(self.Labellabel, 9, 0, 1, 1)
        self.listWidget = ListBox(self.centralwidget)

        # 字体增大
        font = QtGui.QFont()
        font.setPointSize(16);
        font.setWeight(50);
        self.setFont(font)

        self.listWidget.setGeometry(QtCore.QRect(30, 50, 191, 500))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.BtnStart.clicked.connect(MainWindow.Start)
        self.EditMode.clicked.connect(MainWindow.Edit)
        self.BtnPre.clicked.connect(MainWindow.PrePic)
        self.PtnNext.clicked.connect(MainWindow.NextPic)
        self.BtnRec.clicked.connect(MainWindow.DeleteItem)
        self.BtnSave.clicked.connect(MainWindow.Save)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LabelImage.setText(_translate("MainWindow", "Image"))
        self.PtnNext.setText(_translate("MainWindow", "下一张"))
        self.EditMode.setText(_translate("MainWindow", "编辑模式"))
        self.BtnStart.setText(_translate("MainWindow", "开始标注"))
        self.Labelcoor.setText(_translate("MainWindow", "坐标"))
        self.BtnPre.setText(_translate("MainWindow", "上一张"))
        self.BtnRec.setText(_translate("MainWindow", "删除"))
        self.BtnSave.setText(_translate("MainWindow", "保存"))
        self.Labellabel.setText(_translate("MainWindow", "标签"))


