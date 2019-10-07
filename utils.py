import os, cv2
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication

def get_images(path):
    filelist = os.listdir(path)
    filelist = [ele for ele in filelist if ele.endswith('.jpg')]
    return(filelist)

def get_labels(path):
    filelist = os.listdir(path)
    filelist = [ele for ele in filelist if ele.endswith('.txt')]
    return(filelist)

def mat2pix(img):
    height, width, bytesPerComponent = img.shape
    bytesPerLine = 3 * width
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
    QImg = QImage(img.data, width, height, bytesPerLine,QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(QImg)
    return pixmap

if __name__=='__main__':
    path = 'D:\图片'
    get_images(path)