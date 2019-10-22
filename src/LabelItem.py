from utils import coor_trans

class Label:
    def init1(self, _rect, _label, _label_size, _img_size):
        self.P0 = (_rect.x(), _rect.y())
        self.width = _rect.width()
        self.height = _rect.height()
        self.P1 = [self.P0[0]+self.width, self.P0[1]]
        self.P2 = [self.P0[0]+self.width, self.P0[1]+self.height]
        self.P3 = [self.P0[0], self.P0[1]+self.height]
        self.P0_trans = coor_trans(self.P0, _label_size, _img_size)
        self.P1_trans = coor_trans(self.P1, _label_size, _img_size)
        self.P2_trans = coor_trans(self.P2, _label_size, _img_size)
        self.P3_trans = coor_trans(self.P3, _label_size, _img_size)
        self.label = _label

    def init2(self, string, _label_size, _img_size):
        print(_label_size)
        print(_img_size)
        self.str_list = string.split(',')
        self.P0_trans = [int(self.str_list[0]),int(self.str_list[1])]
        self.P1_trans = [int(self.str_list[2]),int(self.str_list[3])]
        self.P2_trans = [int(self.str_list[6]),int(self.str_list[7])]
        self.P3_trans = [int(self.str_list[4]),int(self.str_list[5])]
        self.P0 = coor_trans(self.P0_trans, _img_size, _label_size)
        self.P1 = coor_trans(self.P1_trans, _img_size, _label_size)
        self.P2 = coor_trans(self.P2_trans, _img_size, _label_size)
        self.P3 = coor_trans(self.P3_trans, _img_size, _label_size)
        self.label = self.str_list[8]

    def tofile(self, file):
        print("width:"+str(self.width) + " height:"+str(self.height))
        coor = str(self.P0_trans[0]) + ',' + str(self.P0_trans[1]) + ',' + str(self.P1_trans[0]) + ',' + str(self.P1_trans[1]) + ',' + str(self.P2_trans[0]) + ',' + str(self.P2_trans[1]) + ',' + str(self.P3_trans[0]) + ',' + str(self.P3_trans[1]) + ','
        file.write(coor + self.label +'\n')