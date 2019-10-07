from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtCore import QRect, QPoint, Qt, pyqtSignal, QObject
import sys, cv2
import numpy as np

class LabelSignal(QObject):
    mousemove = pyqtSignal()
    newbox = pyqtSignal()

class ImageLabel(QLabel):
    mouse_flag = False

    TL_point = QPoint(0, 0)
    BR_point = QPoint(0, 0)
    rect_list = []
    label_list = []
    rect_num = 0
    signal = LabelSignal()
    first_img_flag = 0

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
        self.setCursor(Qt.ArrowCursor)

    def mousePressEvent(self, event):
        if(self.rect_num != 0):
            self.signal.newbox.emit()
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
        self.rect_list.append(rect)
        self.signal.mousemove.emit()

    def mouseMoveEvent(self, event):
        if self.mouse_flag:
            self.BR_point = event.globalPos()
            self.BR_point = self.get_Coor(self.BR_point)
            self.update()
            self.signal.mousemove.emit()

    def paintEvent(self, event):
        super().paintEvent(event)
        rect_new = QRect(self.TL_point, self.BR_point)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
        for rect in self.rect_list:
            painter.drawRect(rect)
        painter.drawRect(rect_new)