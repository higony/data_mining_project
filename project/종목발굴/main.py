# 1.1.0 : main 함수를 만들어 파일의 프로젝트화 시작
from selenium import webdriver
from stock_filter import stock_list_by_price, stock_list_by_amount, stock_list_by_purchase, stock_list_by_eliminating, stock_list_by_raise
from list_method import initialize, read_list
import time

# 1.1.1 : 초기화 기능 추가
driver = webdriver.Chrome()

# 1.1.6 : 초기화 멘트 메소드 안에서 출력하도록 수정
initialized_li = initialize(driver)
li = initialized_li

# try:
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
    # 1.1.6 : 등락율 별 필터 기능 추가
    print("6. 등락율 별 필터")
    print("7. 필터 초기화")
    print("8. 필터링 된 종목 조회")
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
        li = stock_list_by_raise(li)
    elif selection == 7:
        # 1.1.6 : 실시간 정보로 수정할 수 있게 변경.
        li = initialize(driver)
        print("초기화가 완료되었습니다.")
    elif selection == 8:
        read_list(li)


# except:
#     print("오류가 발생했습니다.")
# finally:
#     print("프로그램을 종료합니다.")
#     driver.quit()


# api 주소 : https://api.finance.naver.com/siseJson.naver?symbol=217820&requestType=1&startTime=20210423&endTime=20210426&timeframe=day