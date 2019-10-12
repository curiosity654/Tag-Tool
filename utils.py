import os, cv2
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication

def read_resize(path, size):
    img = cv2.imread(path)
    if(type(img) == type(None)):
        return None
    img_size = (img.shape[0], img.shape[1])
    img = cv2.resize(img, size)
    return img, img_size

def coor_trans(Point, label_size, img_size):
    Point_trans = [0,0]
    Point_trans[0] = Point[0]*img_size[0]//label_size[0]
    Point_trans[1] = Point[1]*img_size[1]//label_size[1]
    return Point_trans

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