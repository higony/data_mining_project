from bs4 import BeautifulSoup
import requests

from model import *


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

# 1.0.1: 외인/기관 연속 순매수일 계산
def cal_purchase(li):
    for elem in li:
        res = requests.get(elem.link)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        rows = soup.find("div", attrs={"class":"sub_section right"}).tbody.find_all("tr")[1:-1]
        
        p_f = 0
        f_switch = 1
        p_i = 0
        i_switch = 1
        for day in range(len(rows)):
            if f_switch == i_switch == 0:
                break
            day_info = rows[day].find_all("td")[2:]

            try:
                if f_switch != 0:
                    if int(day_info[0].get_text().replace(",","")) > 0:
                        p_f += 1
                    else:
                        f_switch = 0
            except:
                f_switch = 0

            try:
                if i_switch != 0:
                    if int(day_info[1].get_text().replace(",","")) > 0:
                        p_i += 1
                    else:
                        i_switch = 0
            except:
                i_switch = 0
        elem.input_purchase((p_f, p_i))
    return li