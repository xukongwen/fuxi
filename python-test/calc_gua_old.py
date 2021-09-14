import sys
from pprint import pprint


# 计算八卦第一个版本
def calc_gua(num):
    if num == 0:
        return [0] # 道
    elif num == 1:
        return [[1], [-1]]
    else:
        pre_gua = calc_gua(num - 1)
        new_gua = []
        for gua in pre_gua:
            new_gua.extend([[1] + gua, [-1] + gua])
        return new_gua


if __name__ == "__main__":
    pprint(calc_gua(int(sys.argv[1])))