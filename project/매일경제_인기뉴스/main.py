from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from news_scrapping import *
from CRUD import *

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
    print("기능을 설정해주세요\n")
    print("1. 모든 언론사 top 뉴스 확인하기")
    print("2. 즐겨찾기 설정 (조회 / 등록 / 삭제)") # 1.0.1 추가 예정
    print("3. 즐겨찾는 언론사 top 뉴스 확인하기") # 1.0.1 추가 예정
    print("0. 종료하기")
    selection = int(input("기능선택>>>>>> "))

    if selection == 0:
        break

    elif selection == 1:
        news_print(all_news_scrap(soup))

    # 1.0.1 즐겨찾기 CRUD 기능 추가
    elif selection == 2:
        print("\n1. 즐겨찾기 등록")
        print("2. 즐겨찾기 조회")
        print("3. 즐겨찾기 삭제")
        selection = int(input(">>>> 기능 선택: "))
        if selection == 1:
            favorite_add(press_list, filename)
        elif selection == 2:
            favorite_read(filename)
        elif selection == 3:
            favorite_delete(filename)