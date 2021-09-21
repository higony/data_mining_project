from model import stock
from method import *
from SaveCSV import *

li = cal_purchase(initialize())

# 1.0.1 : 외인/기관 연속 순매수일 계산하기
# 1.0.2 : 외인/기관 수급 포착 시 저장.
"""
저장의 기준
1. 외인 5일 이상 매수 + 기관 3일 이상 매수 : 외인 주도 쌍끌이 매수
2. 외인 3일 이상 매수 + 기관 5일 이상 매수 : 기관 주도 쌍끌이 매수
3. 외인 5일 이상 매수 + 기관 5일 이상 매수 : 양측 주도 쌍끌이 매수
"""
input_list = []
for elem in li:
    if elem.purchase[0] >= 5: # 외인 5일 이상 매수
        if elem.purchase[1] >= 5: # 기관 5일 이상 매수
            input_list.append(["양측 주도 쌍끌이 매수", elem.name, elem.code, elem.price])

        elif elem.purchase[1] >= 3: # 기관 3일 이상 5일 미만 매수
            input_list.append(["외인 주도 쌍끌이 매수", elem.name, elem.code, elem.price])
    
    elif elem.purchase[1] >= 5 and elem.purchase[0] >= 3: # 기관 5일 이상 매수, 외인 3일 이상 5일 미만 매수
        input_list.append(["기관 주도 쌍끌이 매수", elem.name, elem.code, elem.price])



saveCSV(input_list)


