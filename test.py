import codecs
from LabelItem import Label
from utils import coor_trans

with codecs.open('download.txt', 'r', 'utf-8') as file:
    print(file.readline())
    print(file.readline())
    print(string = file.readline() == '')
    # str_list = string.split(',')
    # print((str_list))
    # string = file.readline().strip('\n')
    # str_list = string.split(',')
    # print((str_list))