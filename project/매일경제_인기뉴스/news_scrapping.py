from bs4 import BeautifulSoup
import requests

# 기사 스크래핑과 관련한 메소드

# 모든 기사 스크래핑
def all_news_scrap(soup):
    presses = soup.find_all("div", attrs={"class":"rankingnews_box"})
    result = []

    for press in presses:
        article_titles = []
        article_links = []

        # 언론사 제목
        press_name = press.find("strong").get_text()
        
        # 기사 제목
        article_title = press.find_all("a", attrs={"class":"list_title nclicks('RBP.rnknws')"})
        article_titles += [x.get_text() for x in article_title]
        
        # 기사 링크
        article_links += ["https://news.naver.com" + x["href"] for x in article_title]
        
        # 리스트의 각 element : [언론사, [언론사 내 기사들], [언론사 내 링크들]]
        result.append([press_name, article_titles, article_links])

    return result

# 1.0.2 즐겨찾는 언론사 기사 스크래핑
def favorite_news_scrap(soup, filename):
    with open(filename, "r") as f:
        Mypress = list(set(f.read().split()))

    initial_li = all_news_scrap(soup)
    result = []

    for elem in initial_li:
        if elem[0] in Mypress:
            result.append(elem)
    
    return result
