from MainWindow import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtCore import QRect, QPoint, Qt, pyqtSignal, QObject
import sys, cv2
import numpy as np
from utils import *
from ImageLabel import LabelSignal
import codecs

class window(QMainWindow, Ui_MainWindow):
    
    pic_dir = ""
    img_name = ""
    img = np.zeros(1)
    img_size = (0,0)
    label_size = (0,0)
    img_list = []
    label_list = []
    image_cnt = 0
    start_flag = 0
    saved_flag = 0
    
    def __init__(self):
        super(window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('TagTool')
        self.LabelImage.signal.mousemove.connect(self.setCoor)
        self.LabelImage.signal.newbox.connect(self.resetEt)

    def Start(self):
        self.pic_dir = QFileDialog.getExistingDirectory(self, '选择图片文件夹', "./")
        if(self.pic_dir == ''):
            QMessageBox.about(self,'提示','请选择路径')
            return
        self.img_list = get_images(self.pic_dir)
        self.label_list = get_labels(self.pic_dir)
        if(len(self.img_list) == 0):
            QMessageBox.about(self,'提示','未找到图片')
        else:
            for img in self.img_list:
                if(not (img.strip('.jpg')+'.txt') in self.label_list): #jump to the first img that hasn't been tagged
                    break
                self.image_cnt += 1
                if(self.image_cnt == len(self.img_list)):
                    QMessageBox.about(self,'提示','该文件夹下图片已标注完成')
                    return
            self.img_name = self.pic_dir + '/' + self.img_list[self.image_cnt]
            print(self.img_name)
            self.label_size = (self.LabelImage.size().width(), self.LabelImage.size().height())
            self.img, self.img_size = read_resize(self.img_name, self.label_size)
            # self.img = cv2.imread(self.img_name)
            if(type(self.img) == type(None)):
                QMessageBox.about(self,'提示','图片打开失败')
            else:
                pixmap = mat2pix(self.img)
                self.LabelImage.setPixmap(pixmap)
                self.start_flag = 1
                self.LabelImage.label_start = 1

    def End(self):
        print('End.')

    def PrePic(self):
        if(self.start_flag):
            if(self.image_cnt == 0):
                QMessageBox.about(self,'提示','当前是第一张图片')
            else:
                self.image_cnt -= 1
                self.img_name = self.pic_dir + '/' + self.img_list[self.image_cnt]
                self.img = cv2.imread(self.img_name)
                if(type(self.img) == type(None)):
                    QMessageBox.about(self,'提示','图片打开失败')
                else:
                    self.LabelImage.rect_list = []
                    self.LabelImage.label_list = []
                    pixmap = mat2pix(self.img)
                    self.LabelImage.rect_num = 0
                    self.LabelImage.setPixmap(pixmap)
                    self.saved_flag = 0
                # print('PrePic.')
        else:
            QMessageBox.about(self,'提示','请选择文件夹')

    def NextPic(self):
        if(self.start_flag):
            if(self.image_cnt == len(self.img_list)-1):
                QMessageBox.about(self,'提示','当前是最后一张图片')
            else:
                self.image_cnt += 1
                self.img_name = self.pic_dir + '/' + self.img_list[self.image_cnt]
                self.img = cv2.imread(self.img_name)
                if(type(self.img) == type(None)):
                    QMessageBox.about(self,'提示','图片打开失败')
                else:
                    self.LabelImage.rect_list = []
                    self.LabelImage.label_list = []
                    pixmap = mat2pix(self.img)
                    self.LabelImage.rect_num = 0
                    self.LabelImage.setPixmap(pixmap)
                    self.saved_flag = 0
                # print('NextPic.')
        else:
            QMessageBox.about(self,'提示','请选择文件夹')

    def PreRec(self):
        print('PreRec.')
    
    def Save(self):
        self.resetEt()
        with codecs.open(self.img_name.strip('.jpg')+'.txt', 'w', 'utf-8') as f:
            cnt = 0
            print(self.LabelImage.rect_num)
            for cnt in range(self.LabelImage.rect_num):
                # print(cnt)
                rect = self.LabelImage.rect_list[cnt]
                label = self.LabelImage.label_list[cnt]
                P0 = (rect.x(), rect.y())
                width = rect.width()
                height = rect.height()
                P1 = (P0[0]+width, P0[1])
                P2 = (P0[0], P0[1]+height)
                P3 = (P0[0]+width, P0[1]+height)

                P0_trans = coor_trans(P0, self.label_size, self.img_size)
                P1_trans = coor_trans(P1, self.label_size, self.img_size)
                P2_trans = coor_trans(P2, self.label_size, self.img_size)
                P3_trans = coor_trans(P3, self.label_size, self.img_size)
                print(width, height)
                coor = str(P0_trans[0]) + ',' + str(P0_trans[1]) + ',' + str(P1_trans[0]) + ',' + str(P1_trans[1]) + ',' + str(P2_trans[0]) + ',' + str(P2_trans[1]) + ',' + str(P3_trans[0]) + ',' + str(P3_trans[1])
                f.write(coor + ' Wei ' + label +'\n')
        print('Save.')
        self.saved_flag = 1

    def setCoor(self):
        x0 = self.LabelImage.TL_point.x
        y0 = self.LabelImage.TL_point.y
        x1 = self.LabelImage.BR_point.x
        y1 = self.LabelImage.BR_point.y
        self.EtTLcoor.setText('('+str(x0)+','+str(y0)+')')
        self.EtTRcoor.setText('('+str(x1)+','+str(y0)+')')
        self.EtBLcoor.setText('('+str(x0)+','+str(y1)+')')
        self.EtBRcoor.setText('('+str(x1)+','+str(y1)+')')

    def resetEt(self):
        if(self.saved_flag == 0):
            # print('resetEt')
            label = self.EtLabel.toPlainText()
            if(len(label) == 0):
                QMessageBox.about(self,'提示','请输入标签')
                self.LabelImage.label_list.append('')
            else:
                # print(label)
                self.LabelImage.label_list.append(label)
                self.EtLabel.setPlainText('')
        else:
            self.saved_flag = 0

if __name__=='__main__':
    app = QApplication(sys.argv)
    ui = window()
    ui.show()
    sys.exit(app.exec_())