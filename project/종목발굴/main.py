# 1.1.0 : main 함수를 만들어 파일의 프로젝트화 시작
from selenium import webdriver
from stock_price_rank import stock_list_by_price
from list_method import initialize, read_list
import time

# 1.1.1 : 초기화 기능 추가
driver = webdriver.Chrome()
print("초기화 중입니다.")
initialized_li = initialize(driver)
li = initialized_li
print("초기화를 완료했습니다.")
try:
    while True:
        print("원하시는 필터 적용 및 기능을 선택해주세요.")
        print("1. 가격별 필터")
        # print("2. 거래량 0 제외")
        # print("3. 거래량 별 필터")
        print("4. 필터 초기화")
        print("5. 필터링 된 종목 조회")
        print("0. 종료")
        selection = int(input("기능 선택 >>>>>>> "))
        time.sleep(2)

        if selection == 0:
            break
        elif selection == 1:
            li = stock_list_by_price(li)
        elif selection == 4:
            li = initialized_li
            print("초기화가 완료되었습니다.")
        elif selection == 5:
            read_list(li)
        
        time.sleep(2)
    
except:
    print("오류가 발생했습니다.")
finally:
    print("프로그램을 종료합니다.")
    driver.quit()