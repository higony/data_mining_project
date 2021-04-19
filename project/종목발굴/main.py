# 1.1.0 : main 함수를 만들어 파일의 프로젝트화 시작
from selenium import webdriver
from stock_price_rank import stock_list_by_price
from list_method import read_list

try:
    driver = webdriver.Chrome()
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1" # 코스피인 경우 sosok이 0, 코스닥인 경우 1. page는 몇 번째 페이지인지 나타냄.
    driver.get(url)

    li = stock_list_by_price(driver)
    read_list(li)
    
except:
    print("오류가 발생했습니다.")
finally:
    print("프로그램을 종료합니다.")
    driver.quit()