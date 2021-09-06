from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from news_scrapping import *
from CRUD import *

# 1.1.0 csv 저장 기능 추가 -> 빅데이터화
import csv
# csv 열기
f = open("화제뉴스.csv", "a", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

# 오늘 날짜 정보
import datetime
today = datetime.date.today()
today_str = f"{today.year}-{today.month}-{today.day}"


# 1.0.3 출력 form 개선

# 기본 설정
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"} # 헤더 정보
# driver = webdriver.Chrome()
url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111" # 네이버 뉴스 url
# driver.get(url)
res = requests.get(url, headers=headers) # 네이버 뉴스 url requests
soup = BeautifulSoup(res.text, "lxml") # 네이버 뉴스 url의 html 이용

# 1.0.1 전체 언론사 추가: 즐겨찾기 하기 위한 검색 기능 구현
press_list = []
for elem in all_news_scrap(soup):
    press_list.append(elem[0])
press_list.sort()
filename = "Mypress.txt" # 즐겨찾기 할 파일 이름


# 1.0.0 선택기능 : 언론사별 인기 뉴스
while True:
    print("-"*50)
    print("\n기능을 설정해주세요")
    print("\n 1. 모든 언론사 top 뉴스 확인하기")
    print(" 2. 즐겨찾기 설정 (조회 / 등록 / 삭제)") # 1.0.1 추가 예정
    print(" 3. 즐겨찾는 언론사 top 뉴스 확인하기") # 1.0.1 추가 예정
    print(" 0. 종료하기")
    selection = int(input("\n기능선택 >>>>>> "))

    if selection == 0:
        break
    
    elif selection == 1:
        news_print(all_news_scrap(soup))

    # 1.0.1 즐겨찾기 CRUD 기능 추가
    elif selection == 2:
        print("-"*50)
        print("즐겨찾기 관련한 메뉴들입니다. 원하시는 기능을 선택해주세요.")
        print("\n1. 즐겨찾기 등록")
        print("2. 즐겨찾기 조회")
        print("3. 즐겨찾기 삭제")
        selection = int(input("\n 기능 선택 >>>>>"))
        if selection == 1:
            favorite_add(press_list, filename)
        elif selection == 2:
            favorite_read(filename)
        elif selection == 3:
            favorite_delete(filename)
    
    # 1.1.0 csv 통한 데이터화
    elif selection == 3:
        result_li = favorite_news_scrap(soup,filename)
        news_print(result_li)

        print("\n출력된 언론사들을 저장할까요?\n")
        print("1. Yes")
        print("2. No")
        selection = int(input("\n선택 >>>>> "))
        print()
        if selection == 1:
            save_csv(result_li, today_str, writer)
            


f.close()