from bs4 import BeautifulSoup
# 1.1.0 : 종목 정보가 포함된 list를 다루는 메소드 모음.

def sort_list(li): # 1.1.3 : 리스트 정렬하는 기능 구현
    try:
        print("분류하고자 하는 기준을 설정해주세요.")
        print("1. 종목명\t2.현재가\t3.등락율\t4.거래량")
        selection = int(input(">>>>> 기준 선택 : "))
        print("오름차순 / 내림차순을 설정합니다. 원하는 옵션을 선택해주세요.")
        print("1. 오름차순\t2. 내림차순")
        orderby = int(input(">>>>> 옵션 선택 : "))
        if orderby == 1:
            li = sorted(li, key=lambda x:x[selection-1])
        else: li = sorted(li, key=lambda x:x[selection-1], reverse=True)
    except:
        print("오류가 발생하였습니다. 기본 설정으로 정렬합니다.")
    finally:
        return li
    
def read_list(li):
    # li 안의 각 요소들의 형태 : (종목명, 현재가, 등락, 거래량, 링크)
    temp_li = sort_list(li)
    length = len(temp_li)
    print(f"총 {length}개의 검색 결과가 있습니다.")
    for i in range(length):
        print(f"{i+1}. {temp_li[i][0]} : {temp_li[i][4]}")
        print(f"현재가 {temp_li[i][1]}원 ({temp_li[i][2]}%)\t거래량 {temp_li[i][3]}")
        print("-"*100)

def initialize(driver): # 1.1.1 : 초기화 함수 구현
    li = [] # 각 종목별 종목명, 현재가, 등락, 거래량, 링크를 가져오고자 함.
    for sosok in range(2):
        default_url = f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok={sosok}"
        driver.get(default_url)
        driver.find_element_by_class_name('pgRR').click()
        pages = int(driver.current_url[-2:])
        for page in range(1,pages+1):
            url = default_url + f"&page={page}"
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, "lxml")
            table_elements = soup.find("table", attrs={"class":"type_2"}).tbody.find_all("tr", attrs={"onmouseover":"mouseOver(this)"})
            for element in table_elements: # 필요한 정보: 종목명, 현재가, 등락, 거래량, 링크.
                link = "https://finance.naver.com" + element.find("a")["href"]
                info = list([x.get_text().strip() for x in element.find_all("td")])
                title = info[1]
                current_price = int(info[2].replace(",",""))
                percentage = float(("".join(info[4].split()))[:-1])
                amount = int(info[9].replace(",",""))
                info_tuple = (title, current_price, percentage, amount, link)
                li.append(info_tuple)
    return li




