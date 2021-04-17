from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv
import datetime
# 1.0.2 : 폴더 위치 변경
options = webdriver.ChromeOptions()
options.headless=True
options.add_argument("window-size=2560x1600")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")
driver = webdriver.Chrome(options=options) # 1.0.1 : headless chrome 구현

url = "https://comic.naver.com/webtoon/weekday.nhn"
driver.get(url)
driver.minimize_window()
soup = BeautifulSoup(driver.page_source, "lxml")

filename = "논란웹툰정리.csv"
f = open(filename, "a", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

today = datetime.date.today()
today_str = f"{today.year}-{today.month}-{today.day}"

def find_rate(cartoon_link): # 평점의 평균을 반환하는 함수 
    a = 0
    latest_rate = 0
    cnt = 0
    res = requests.get(cartoon_link)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    rating_box = soup.find_all("div", attrs={"class":"rating_type"})
    webtoon_head = soup.find("td", attrs={"class":"title"}).a.get_text()
    for ratings in rating_box:
        cnt += 1
        rating = float(ratings.find("strong").get_text())
        a += rating
        if cnt == 1:
            latest_rate = rating
    return [latest_rate, a/len(rating_box), webtoon_head]

def find_comments(webtoon_link):
    driver.get(webtoon_link)
    soup = BeautifulSoup(driver.page_source, "lxml")
    comment_link = ("https://comic.naver.com" + soup.find("td", attrs={"class":"title"}).a["href"]).replace("webtoon/detail", "comment/comment")
    driver.get(comment_link)
    soup = BeautifulSoup(driver.page_source, "lxml")
    best_comments = soup.find_all("span", attrs={"class": "u_cbox_contents"})
    li = []
    for best_comment in best_comments:
        li.append(best_comment.get_text())
    result = "\n".join(li)
    return result


webtoon_list = soup.find("div", attrs={"class": "col col_selected"})
webtoon_info = webtoon_list.find_all("a", attrs={"class":"title"})

for webtoon in webtoon_info:
    webtoon_title = webtoon.get_text()
    webtoon_link = "https://comic.naver.com" + webtoon["href"]
    rate_list = find_rate(webtoon_link)
    rate_difference = rate_list[0]-rate_list[1]
    webtoon_head = rate_list[2]
    
    if rate_difference <= -0.5 or rate_list[0] < 8: # 1.0.1 : 평점 차이와 관련 없이 평점이 8 미만이어도 잡아내도록 설정
        print(webtoon_title, ":", webtoon_link)
        print("     별점 차이: %.2f" %(rate_list[0]-rate_list[1]))
        comments = find_comments(webtoon_link)
        info = [today_str, webtoon_title, webtoon_head, rate_list[0], rate_list[1], rate_difference, webtoon_link, comments]
        writer.writerow(info)
        print("*"*100)

driver.quit()