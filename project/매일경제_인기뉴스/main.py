from bs4 import BeautifulSoup
from selenium import webdriver
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

# driver = webdriver.Chrome()
url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
# driver.get(url)
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "lxml")


presses = soup.find_all("div", attrs={"class":"rankingnews_box"})

for idx, press in enumerate(presses):
    press_name = press.find("strong").get_text()
    articles = press.find_all("a", attrs={"class":"list_title nclicks('RBP.rnknws')"})
    
    print(f"{idx+1}) {press_name}")
    for a_idx, article in enumerate(articles):
        print(f"  {a_idx+1}. {article.get_text()}")

    print()