from bs4 import BeautifulSoup
import requests

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

# 모든 기사 결과 출력
def news_print(li):
    for idx, elem in enumerate(li):
        print(f"{idx+1}) {elem[0]}")

        for k in range(len(elem[1])):
            print(f"  {k+1}. {elem[1][k]}")
            print(f"  링크: {elem[2][k]}")
            print()
        print("-"*50, end="\n\n")