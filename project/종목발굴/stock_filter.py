# 1.1.0 : main 함수 내에서 동작하는 메소드로 정의.
# 1.1.1 : 리스트를 통하여 스크래핑 진행.
# 1.1.2 : 거래량 기준 필터 기능 추가
# 1.1.4 : 외인 / 기관 연일 순매수 필터 기능 추가
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta

def finalize(li):
    print("검색을 종료합니다. ", end="")
    print(f"총 {len(li)}개의 검색 결과가 있습니다.")

def stock_list_by_price(li):
# 1.0.2 : 원하는 가격대의 종목을 확인할 수 있도록 하는 기능 구현 + 예외 처리
# 1.1.2 : 메소드 영역에서 예외 처리 기능 삭제
    minimum_price = int(input("조회를 원하는 종목의 최소 가격을 입력해주세요: "))
    maximum_price = int(input("조회를 원하는 종목의 최대 가격을 입력해주세요: "))
    result = []
    for element in li: # 필요한 정보 : 가격. index num 1
        if element[1] not in range(minimum_price, maximum_price+1): # 주가가 원하는 범위 내가 아니라면,
            continue
        result.append(element)
    finalize(result)
    return result

def stock_list_by_amount(li):
    minimum_amount = int(input("조회를 원하는 종목의 최소 거래량을 입력해주세요: "))
    maximum_amount = input("조회를 원하는 종목의 최대 거래량을 입력해주세요. 설정을 원하지 않으시다면 엔터키를 눌러주세요: ")
    # 필요한 정보: 거래량. index num 3
    if maximum_amount == "":
        ifs = 1
    else:
        maximum_amount = int(maximum_amount)
        ifs = 2
    
    result = []
    for element in li:
        if ifs == 1 and element[3] < minimum_amount:
            continue
        elif ifs == 2 and element[3] not in range(minimum_amount, maximum_amount+1):
            continue
        result.append(element)
    finalize(result)
    return result

# 1.1.4 : 외인 / 기관 연일 순매수 필터 기능 추가
def stock_list_by_purchase(li, selection): # selection = 1이면 외인, 2면 기관 매수
    num = 10
    init_percentage = float(len(li)) / num
    percentage = init_percentage
    cnt = 0
    if selection == 1:
        col_num = 2
    else: col_num = 3
    result = []
    purchase_days = int(input("최근 몇일 연속 순매수한 종목을 찾고 싶으신지 입력해주세요(최대 6일까지 가능): "))
    if purchase_days not in range(1,7):
        print("잘못된 일수를 입력하셨습니다. 함수를 종료합니다.")
        return
    
    for elem in li:
        print(elem[0])
        cnt += 1
        res = requests.get(elem[4])
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        table = soup.find("div", attrs={"class":"sub_section right"}).find("table").tbody.find_all("tr")[1:-1]
        if not table:
            continue
        for day in range(purchase_days):
            try:
                purchase_amounts = int(table[day].find_all("td")[col_num].get_text().strip().replace(",",""))
                if purchase_amounts < 0:
                    break
            except:
                source = table[day].find("em", attrs={"class":"sam"})
                if source:
                    break
                day = purchase_days - 1
            if day == purchase_days - 1:
                result.append(elem)
        # 1.1.5 : 시간이 오래걸리는 기능에 대해 각 퍼센트별로 진행 상황 브리핑 기능 추가
        if cnt >= percentage:
            print(f"{num}% 검색을 완료하였습니다.")
            num += 10
            percentage += init_percentage
    finalize(result)
    return result

# 1.1.5 : 스팩, ETF, ETN 제외 필터 추가
# 1.1.7 : 정확도 100%로 설정하기 위해 반복문 추가.
def stock_list_by_eliminating(li, driver):
    url_list = [
        'https://finance.naver.com/sise/etf.nhn',
        'https://finance.naver.com/sise/etn.nhn',
        'https://finance.naver.com/search/searchList.nhn?query=%BD%BA%C6%D1'
    ]
    print("제외하고자 하는 종목의 분류를 선택해주세요.")
    selection = int(input("1. ETF\n2. ETN\n3. 스팩\n>>>>>선택하기: "))
    eleminating_url = url_list[selection-1]
    eleminating_set = set({})
    for cnt in range(4):
        if selection == 3:
            for idx, elem in enumerate(li):
                if "스팩" in elem[0]:
                    del li[idx]
        
        else:    
            driver.get(eleminating_url)
            soup = BeautifulSoup(driver.page_source, "lxml")
            title_list = soup.find_all("td", attrs={"class":"ctg"})
            for title_info in title_list:
                title = title_info.get_text().strip()[:5]
                eleminating_set.add(title)

            for idx, elem in enumerate(li):
                if elem[0][:5] in eleminating_set:
                    del li[idx]

    finalize(li)
    return li

# 1.1.6 : 등락율을 기준으로 필터링하는 기능 추가.
def stock_list_by_raise(li):
    today = datetime.today()
    today_str = today.strftime("%Y%m%d")
    days = int(input("며칠 사이의 등락율을 검색하실지 입력해주세요. "))
    criteria_day = today - timedelta(days=days)
    criteria_day_str = criteria_day.strftime("%Y%m%d")

    minimum_raise = float(input("조회를 원하는 종목의 최소 등락율을 입력해주세요. (마이너스 가능): "))
    maximum_raise = float(input("조회를 원하는 종목의 최대 등락율을 입력해주세요. (마이너스 가능): "))

    result = []

    for elem in li:
        code = elem[4][-6:]
        url = f"https://api.finance.naver.com/siseJson.naver?symbol={code}&requestType=1&startTime={criteria_day_str}&endTime={today_str}&timeframe=day"
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        text = soup.get_text().replace(", ",",").split()
        temp_prices = [text[1], text[-2]]
        raises = []
        for x in temp_prices:
            price = int(x.split(",")[4])
            raises.append(price)
        percentage = (float(raises[1] - raises[0]) / raises[0]) * 100
        if percentage >= minimum_raise and percentage <= maximum_raise:
            result.append(elem)
    finalize(result)
    return result

    # ", " -> ","로 replace한 뒤, split 진행 -> 1, -2번째 인덱스를 기준으로 비교.
    # 각 요소들에서 []기호를 빼고 ","기준으로 split. 이때 기준 4번째 idx가 종가.