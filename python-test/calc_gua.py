import sys
import json 
from pprint import pprint


class  GuaCalculator(object):

    def  __init__(self, gua_num=1):
        self.gua_num = gua_num
        self.gua_pos_max = 2 ** gua_num

    @classmethod
    def _calc_yy(cls, gua_num, gua_pos, gua_pos_max):
        mid_pos = gua_pos_max // 2
        if gua_num == 1:
            return -1 if gua_pos > mid_pos else 1
        if gua_pos > mid_pos:
            new_gua_pos = gua_pos % mid_pos
            if new_gua_pos == 0:
                new_gua_pos = mid_pos
            return cls._calc_yy(gua_num -  1, new_gua_pos, mid_pos)
        else:
            return cls._calc_yy(gua_num -  1, gua_pos, mid_pos)
        
    def __call__(self, gua_pos=1):
        gua = []
        for num in range(self.gua_num, 0, -1):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
            gua.append(self._calc_yy(num, gua_pos, self. gua_pos_max))
        return gua


def calc_gua(num):
    calc = GuaCalculator(num)
    gua = []
    for i in range(calc.gua_pos_max):
        gua.append(calc(i))
    return gua


if __name__ == "__main__":
   # calc = GuaCalculator(int(sys.argv[1]))
   # pprint(calc(int(sys.argv[2])))
#    pprint(calc_gua(int(sys.argv[1])))
    num = int(sys.argv[1])
    json.dump(calc_gua(num), open("gua-{}.json".format(num), "w"))