from MainWindow_2 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtCore import QRect, QPoint, Qt, pyqtSignal, QObject
import sys, cv2
import numpy as np
from utils import *
import codecs
from LabelItem import Label
import os.path

class window(QMainWindow, Ui_MainWindow):
    
    pic_dir = ""
    img_name = ""
    img = np.zeros(1)
    img_files = []              # 选中路径下图片文件名列表
    label_files = []            # 选中路径下标签文件名列表       
    image_cnt = 0
    start_flag = 0
    saved_flag = 0
    img_size = (0,0)
    label_size = (0,0)
    edit_mode = False
    
    def __init__(self):
        super(window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('TagTool-标记模式')
        self.LabelImage.label_list = []
        self.LabelImage.signal.mousemove.connect(self.setCoor)
        self.LabelImage.signal.newbox.connect(self.resetEt)
        self.listWidget.itemClicked.connect(self.labelClicked)
        self.window().EditMode.clicked.connect(self.LabelImage.Edit)

    def Start(self):
        pic_dir = QFileDialog.getExistingDirectory(self, '选择图片文件夹', "./")
        if(pic_dir == ''):
            QMessageBox.about(self,'提示','请选择路径')
            return
        self.pic_dir = pic_dir
        self.img_files = get_images(self.pic_dir)
        self.label_files = get_labels(self.pic_dir)
        if(len(self.img_files) == 0):
            QMessageBox.about(self,'提示','未找到图片')
        else:
            self.image_cnt = 0

            #jump to the first img that hasn't been tagged
            # for img in self.img_files:
            #     if(not (img.strip('.jpg')+'.txt') in self.label_files): 
            #         break
            #     self.image_cnt += 1
            #     if(self.image_cnt == len(self.img_files)):
            #         QMessageBox.about(self,'提示','该文件夹下图片已标注完成')
            #         return

            self.img_name = self.pic_dir + '/' + self.img_files[self.image_cnt]
            print(self.img_name)
            self.label_size = (self.LabelImage.size().width(), self.LabelImage.size().height())
            self.img, self.img_size = read_resize(self.img_name, self.label_size)
            print(self.label_size, self.img_size)
            if(type(self.img) == type(None)):
                QMessageBox.about(self,'提示','图片打开失败')
            else:
                self.LabelImage.label_list = self.window().listWidget.Load_data2(self.img_name.strip('.jpg')+'.txt', self.label_size, self.img_size)
                self.LabelImage.loadLabels()
                pixmap = mat2pix(self.img)
                self.LabelImage.setPixmap(pixmap)
                self.start_flag = 1
                self.LabelImage.label_start = 1
                self.LabelImage.flag_delete = 0;

    def Edit(self):
        if(self.start_flag):
            print(self.edit_mode)
            if(not self.edit_mode):
                file_name = self.img_name.strip('.jpg')+'.txt'
                if(not os.path.isfile(file_name)):
                    QMessageBox.about(self,'提示','当前图片未标注，无法进入编辑模式')
                    return
                else:
                    self.edit_mode = True
                    self.setWindowTitle('TagTool-编辑模式')
                    self.window().EditMode.setText('标注模式')
                    self.LabelImage.update()
            else:
                self.edit_mode = False
                self.setWindowTitle('TagTool-标注模式')
                self.window().EditMode.setText('编辑模式')
                self.LabelImage.update()
            
        else:
            QMessageBox.about(self,'提示','请选择文件夹')

    def PrePic(self):
        if(self.start_flag):
            if(self.image_cnt == 0):
                QMessageBox.about(self,'提示','当前是第一张图片')
            else:
                self.image_cnt -= 1
                self.img_name = self.pic_dir + '/' + self.img_files[self.image_cnt]
                self.img, self.img_size = read_resize(self.img_name, self.label_size)
                if(type(self.img) == type(None)):
                    QMessageBox.about(self,'提示','图片打开失败')
                else:
                    self.LabelImage.label_list = []
                    self.LabelImage.rect_list = []
                    self.LabelImage.string_list = []
                    self.LabelImage.label_list = self.window().listWidget.Load_data2(self.img_name.strip('.jpg')+'.txt', self.label_size, self.img_size)
                    self.LabelImage.loadLabels()
                    pixmap = mat2pix(self.img)
                    self.LabelImage.rect_num = 0
                    self.LabelImage.setPixmap(pixmap)
                    self.EtLabel.setPlainText('')
                    self.saved_flag = 0
                    self.LabelImage.clicked_label = -1
                    self.LabelImage.flag_delete = 0;
                # print('PrePic.')
        else:
            QMessageBox.about(self,'提示','请选择文件夹')

    def NextPic(self):
        if(self.start_flag):
            if(self.image_cnt == len(self.img_files)-1):
                QMessageBox.about(self,'提示','当前是最后一张图片')
            else:
                self.image_cnt += 1
                self.img_name = self.pic_dir + '/' + self.img_files[self.image_cnt]
                self.img, self.img_size = read_resize(self.img_name, self.label_size)
                if(type(self.img) == type(None)):
                    QMessageBox.about(self,'提示','图片打开失败')
                else:
                    self.LabelImage.rect_list = []
                    self.LabelImage.string_list = []
                    self.LabelImage.label_list = self.window().listWidget.Load_data2(self.img_name.strip('.jpg')+'.txt', self.label_size, self.img_size)
                    self.LabelImage.loadLabels()
                    pixmap = mat2pix(self.img)
                    self.LabelImage.rect_num = 0
                    self.LabelImage.setPixmap(pixmap)
                    self.EtLabel.setPlainText('')
                    self.saved_flag = 0
                    self.LabelImage.clicked_label = -1
                    self.LabelImage.flag_delete = 0
                # print('NextPic.')
        else:
            QMessageBox.about(self,'提示','请选择文件夹')

    def DeleteItem(self):
        if(self.LabelImage.edit_mode):
            if(self.LabelImage.clicked_label == -1):
                QMessageBox.about(self,'提示','请选择标签')
                return
            for i in range(self.listWidget.count()):
                    if(self.listWidget.item(i).isSelected()):
                        del self.LabelImage.rect_list[i]
                        del self.LabelImage.string_list[i]
                        deletelistitem = self.window().listWidget.item(i)
                        self.window().listWidget.takeItem(self.window().listWidget.row(deletelistitem))
                        self.window().EtLabel.setPlainText('')
                        self.LabelImage.rect_num -= 1
                        self.LabelImage.clicked_label = -1
                        self.LabelImage.update()
                        print('DeleteItem.')
                        self.LabelImage.flag_delete = 1;
                        return
        else:
            QMessageBox.about(self,'提示','请在编辑模式下删除标签')
    
    def Save(self):
        if(not self.LabelImage.flag_delete):
            print('reset')
            label = self.EtLabel.toPlainText()
            if(len(label) == 0):
                QMessageBox.about(self,'提示','请输入标签')
                return
            self.resetEt()
            if(len(self.LabelImage.rect_list) == 0):
                QMessageBox.about(self,'提示','当前图片无可保存标注')
                return
        
        with codecs.open(self.img_name.strip('.jpg')+'.txt', 'w', 'utf-8') as f:
            cnt = 0
            print(str(len(self.LabelImage.rect_list))+" rects in total.")
            for cnt in range(len(self.LabelImage.rect_list)):
                rect = self.LabelImage.rect_list[cnt]
                label = self.LabelImage.string_list[cnt]
                label_item = Label()
                label_item.init1(rect, label, self.label_size, self.img_size)
                label_item.tofile(f)
        print('Save.')
        self.LabelImage.flag_delete = 0;
        self.LabelImage.update()
        self.window().listWidget.Load_data2(self.img_name.strip('.jpg')+'.txt', self.label_size, self.img_size)
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
            else:
                # print(label)
                if(self.edit_mode):
                    if(len(self.LabelImage.rect_list) == 0):
                        QMessageBox.about(self,'提示','当前图片无可修改标注，请在标注模式下标注')
                        return
                    self.LabelImage.string_list[self.LabelImage.clicked_label] = label
                else:
                    self.LabelImage.string_list.append(label)
                if(not self.edit_mode):
                    self.EtLabel.setPlainText('')
                self.window().listWidget.Load_data1(self.LabelImage.rect_list, self.LabelImage.string_list, self.label_size, self.img_size)
        else:
            self.saved_flag = 0

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if(event.key() == Qt.Key_S):
            if QApplication.keyboardModifiers() == Qt.ControlModifier:
                self.Save()
        if(event.key() == Qt.Key_A):
            if QApplication.keyboardModifiers() == Qt.ControlModifier:
                self.PrePic()
        if(event.key() == Qt.Key_D):
            if QApplication.keyboardModifiers() == Qt.ControlModifier:
                self.NextPic()

    def labelClicked(self, item):
        if(self.edit_mode):
            for i in range(self.listWidget.count()):
                if(self.listWidget.item(i).isSelected()):
                    self.LabelImage.clicked_label = i
                    self.EtLabel.setPlainText(self.LabelImage.string_list[i])
                    print('item '+item.text()+' clicked.')
                    self.LabelImage.update()
                    return

if __name__=='__main__':
    app = QApplication(sys.argv)
    ui = window()
    ui.show()
    sys.exit(app.exec_())