from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QListWidget
from LabelItem import Label
import codecs
import os.path

class ListBox(QListWidget):
    def Load_data(self, label_file, label_size, img_size):
        self.clear()
        label_list = []
        if(not os.path.isfile(label_file)): return label_list
        with codecs.open(label_file, 'r', 'utf-8') as file:
            while(True):
                string = file.readline().strip('\n')
                if(string == ''): break
                label = Label()
                label.init2(string, label_size, img_size)
                self.addItem(label.label)
                label_list.append(label)
        print(label_list)
        return label_list