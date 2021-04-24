# 1.1.0 : main 함수를 만들어 파일의 프로젝트화 시작
from selenium import webdriver
from stock_filter import stock_list_by_price, stock_list_by_amount, stock_list_by_purchase, stock_list_by_eliminating
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
        # 1.1.2 : 거래량 기준 필터 기능 추가
        print("2. 거래량 별 필터")
        # 1.1.4 : 외인 / 기관 연일 순매수 필터 기능 추가
        print("3. 외인 순매수 별 필터")
        print("4. 기관 순매수 별 필터")
        # 1.1.5 : ETF, ETN, 스팩 종목 제외 필터 기능 추가
        print("5. ETF, ETN, 스팩 종목 제외 필터")
        print("6. 필터 초기화")
        print("7. 필터링 된 종목 조회")
        print("0. 종료")
        selection = int(input("기능 선택 >>>>>>> "))


        if selection == 0:
            break
        elif selection == 1:
            li = stock_list_by_price(li)
        elif selection == 2:
            li = stock_list_by_amount(li)
        elif selection == 3:
            li = stock_list_by_purchase(li, 1)
        elif selection == 4:
            li = stock_list_by_purchase(li, 2)
        elif selection == 5:
            li = stock_list_by_eliminating(li, driver)
        elif selection == 6:
            li = initialized_li
            print("초기화가 완료되었습니다.")
        elif selection == 7:
            read_list(li)


except:
    print("오류가 발생했습니다.")
finally:
    print("프로그램을 종료합니다.")
    driver.quit()


# api 주소 : https://api.finance.naver.com/siseJson.naver?symbol=217820&requestType=1&startTime=20200710&endTime=20210422&timeframe=day