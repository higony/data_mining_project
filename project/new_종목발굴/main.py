from model import stock
from method import *

li = cal_purchase(initialize())

# 1.0.1 : 외인/기관 연속 순매수일 계산하기

for elem in li:
    if elem.purchase[0] >= 3 and elem.purchase[1] >= 3:
        elem.print()