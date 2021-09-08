from selenium import webdriver
from bs4 import BeautifulSoup
import requests

from model import *

options = webdriver.ChromeOptions()
options.headless=True
options.add_argument("window-size=2560x1600")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")
driver = webdriver.Chrome(options=options)

def initialize():
    result = []
    for sosok in range(2):
        url = f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok={sosok}"
        res = requests.get(url)

        soup = BeautifulSoup(res.text, "lxml")
        
        all_pages = int(soup.find("td", attrs={"class":"pgRR"}).a["href"][-2:])

        for page in range(1, all_pages+1):
            url = f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok={sosok}&page={page}"
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "lxml")
            
            stock_list = soup.find("tbody").find_all("tr", attrs={"onmouseout":"mouseOut(this)"})
            for stock_info in stock_list:
                name_info = stock_info.find("a", attrs={"class":"tltle"})
                name = name_info.get_text()
                link = "https://finance.naver.com" + name_info["href"]
                
                number_info = stock_info.find_all("td", attrs={"class":"number"})
                price = int(number_info[0].get_text().replace(",",""))
                updown = float(number_info[2].get_text().strip()[:-1])
                amount = int(number_info[7].get_text().replace(",",""))

                result.append(stock(name, price, updown, amount, link))

    return result
