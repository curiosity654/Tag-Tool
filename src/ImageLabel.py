from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtCore import QRect, QPoint, Qt, pyqtSignal, QObject
import sys, cv2
import numpy as np

class Signals(QObject):
    mousemove = pyqtSignal()
    newbox = pyqtSignal()

class ImageLabel(QLabel):
    mouse_flag = False

    TL_point = QPoint(0, 0)
    BR_point = QPoint(0, 0)
    rect_list = []
    string_list = []
    label_list = []             # LabelItem 类的对象列表，用于保存
    clicked_label = -1
    rect_num = 0
    signal = Signals()
    first_img_flag = 0
    label_start = 0
    edit_mode = 0
    flag_delete = 0

    def get_Coor(self, Point): # imporve to avoid coor exceed the pic
        Point = self.mapFromGlobal(Point)
        xoffset = (self.contentsRect().width()-self.pixmap().rect().width())//2
        yoffset = (self.contentsRect().height()-self.pixmap().rect().height())//2
        Point.x = Point.x()-xoffset
        Point.y = Point.y()-yoffset
        # print(Point)
        return Point

    # Set cursor shape
    def enterEvent(self, event):
        self.setCursor(Qt.CrossCursor)
    
    def leaveEvent(self, event):
        self.mouse_flag = False
        self.setCursor(Qt.ArrowCursor)

    def mousePressEvent(self, event):
        if(self.label_start == 0):
            QMessageBox.about(self,'提示','请选择文件夹')
            return
        if(self.rect_num != 0):
            self.signal.newbox.emit()
        if(not self.edit_mode):
            self.rect_num += 1
        self.mouse_flag = True
        self.TL_point = event.globalPos()
        self.TL_point = self.get_Coor(self.TL_point)
        self.signal.mousemove.emit()

    def mouseReleaseEvent(self, event):
        self.BR_point = event.globalPos()
        self.BR_point = self.get_Coor(self.BR_point)
        self.mouse_flag = False
        rect = QRect(self.TL_point, self.BR_point)
        if(self.edit_mode and len(self.rect_list) > 0):    
            self.rect_list[self.clicked_label] = rect
        else:
            self.rect_list.append(rect)

        self.signal.mousemove.emit()

    def mouseMoveEvent(self, event):
        if self.mouse_flag:
            self.BR_point = event.globalPos()
            self.BR_point = self.get_Coor(self.BR_point)
            self.update()
            self.signal.mousemove.emit()

    def paintEvent(self, event):
        print('paint')
        super().paintEvent(event)
        rect_new = QRect(self.TL_point, self.BR_point)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
        for rect in self.rect_list:
            painter.drawRect(rect)
        if(self.edit_mode and self.clicked_label != -1):
            if(len(self.rect_list)>0):
                print(self.clicked_label)
                painter.setPen(QPen(Qt.yellow,3,Qt.SolidLine))
                painter.drawRect(self.rect_list[self.clicked_label])
        if(self.mouse_flag):
            painter.setPen(QPen(Qt.blue,3,Qt.SolidLine))
            painter.drawRect(rect_new)

    def loadLabels(self):
        rect_list = []
        string_list = []
        if(len(self.label_list) != 0):
            for label in self.label_list:
                p0 = QPoint(label.P0[0], label.P0[1])
                p1 = QPoint(label.P3[0], label.P3[1])
                rect = QRect(p0,p1)
                self.rect_list.append(rect)
                self.string_list.append(label.label)
        self.update()

    def Edit(self):
        self.edit_mode = not self.edit_mode
    # def labelClicked(self, item):
    #     for i in range(len(self.label_list)):
    #         if(item.text() == self.label_list[i].label):
    #             self.clicked_label = i
    #             self.setPlainText(self.label_list[i].label)
    #             print('item '+item.text()+' clicked.')
    #             self.update()