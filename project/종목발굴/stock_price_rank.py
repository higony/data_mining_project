from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1" # 코스피인 경우 sosok이 0, 코스닥인 경우 1. page는 몇 번째 페이지인지 나타냄.
driver.get(url)

driver.find_element_by_class_name("pgRR").click()
pages = int(driver.current_url[-2:]) # 전체 페이지 수

f = open("result.txt", "w")

cnt = 0

try: # 1.0.2 : 원하는 가격대의 종목을 확인할 수 있도록 하는 기능 구현 + 예외 처리
    minimum_price = int(input("조회를 원하는 종목의 최소 가격을 입력해주세요: "))
    maximum_price = int(input("조회를 원하는 종목의 최대 가격을 입력해주세요: "))

    for sosok in range(2):
        for page in range(1, pages+1):
            url = f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok={sosok}&page={page}"
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, "lxml")
            table_elements = soup.find("table", attrs={"class":"type_2"}).tbody.find_all("tr", attrs={"onmouseover":"mouseOver(this)"})
            for element in table_elements: # 필요한 정보: 종목명, 현재가, 거래량
                info = list([x.get_text().strip() for x in element.find_all("td")])
                # 종목명은 1번째, 현재가는 2번째, 거래량은 9번째 요소.
                info_tuple = cnt, info[1], int(info[2].replace(",","")), int(info[9].replace(",",""))

                if info_tuple[3] == 0: # 거래량이 0이라면. 즉, 거래정지된 종목이라면.
                    continue
                if info_tuple[2] > maximum_price or info_tuple[2] < minimum_price: # 주가가 원하는 범위 내가 아니라면,
                    continue
                cnt += 1
                string = f"""
{info_tuple[0]}. {info_tuple[1]}
{info_tuple[2]}원, 거래량: {info_tuple[3]}
""" + "-"*100 + "\n"
                print(string, end="")
                f.write(string)

    f.close()
except:
    print("오류가 발생했습니다.")
finally:
    print("프로그램을 종료합니다.")
    driver.quit()    