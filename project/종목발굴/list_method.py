from bs4 import BeautifulSoup
# 1.1.0 : 종목 정보가 포함된 list를 다루는 메소드 모음.
def read_list(li):
    # li 안의 각 요소들의 형태 : (종목명, 현재가, 등락, 거래량, 링크)
    length = len(li)
    print(f"총 {length}개의 검색 결과가 있습니다.")
    for i in range(length):
        print(f"{i+1}. {li[i][0]} : {li[i][4]}")
        print(f"현재가 {li[i][1]}원 ({li[i][2]}%)\t거래량 {li[i][3]}")
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




