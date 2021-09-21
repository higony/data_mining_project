# 1.0.3 특정 폴더 내 csv에 저장하는 코드 구현
import datetime
import csv
import os
from bs4 import BeautifulSoup
import requests

# 오늘 날짜 "yyyymmdd" 형식으로 나타내기
today = datetime.datetime.today()
today_info = [str(x) for x in [today.year, today.month, today.day]]
for idx in range(1,3):
    if len(today_info[idx]) == 1:
        today_info[idx] = "0" + today_info[idx]
today_str = "".join(today_info)
path = "C:\\Users\\jenis\\Desktop\\깃허브\\project\\new_종목발굴\\"
save_reason = ["외인 주도 쌍끌이 매수", "기관 주도 쌍끌이 매수", "양측 주도 쌍끌이 매수"]
default_link = "https://finance.naver.com/item/main.naver?code="


# 0일, 5일, 20일, 60일, 120일에 대한 종목 정보를 일괄적으로 저장하기
def saveCSV(li):
    saveCSV_120()
    saveCSV_60()
    saveCSV_20()
    saveCSV_10()
    saveCSV_5()
    saveCSV_0(li)

# 0일차 최초 수급 발견한 종목 정보 저장하기
def saveCSV_0(li):
    with open(f"{path}\\0\\{today_str}.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        for elem in li:
            data = [save_reason.index(elem[0]), elem[1], elem[2], elem[3]]
            writer.writerow(data)

def saveCSV_5(): # 단기
    li = sorted(os.listdir(f"{path}0\\"))
    if len(li) >= 5:
        with open(f"{path}\\0\\{li[len(li)-5]}", "r", encoding="utf-8-sig") as f:
            with open(f"{path}\\5\\{li[len(li)-5][:-4]}_5.csv", "w", encoding="utf-8-sig", newline="") as f_w:
                reader = csv.reader(f)
                writer = csv.writer(f_w)
                for line in reader:
                    url = default_link + line[2]
                    res = requests.get(url)
                    soup = BeautifulSoup(res.text, "lxml")
                    price_now = int(soup.find("p", attrs={"class":"no_today"}).find("span", attrs={"class":"blind"}).get_text().replace(",",""))
                    updown = (price_now - int(line[3]))/float(int(line[3]))
                    
                    line.extend([price_now, updown])
                    writer.writerow(line)

def saveCSV_10(): # 중단기
    li = sorted(os.listdir(f"{path}5\\"))
    if len(li) >= 5:
        with open(f"{path}\\5\\{li[len(li)-5]}", "r", encoding="utf-8-sig") as f:
            with open(f"{path}\\10\\{li[len(li)-5][:-4]}_10.csv", "w", encoding="utf-8-sig", newline="") as f_w:
                reader = csv.reader(f)
                writer = csv.writer(f_w)
                for line in reader:
                    del line[-1]
                    url = default_link + line[2]
                    res = requests.get(url)
                    soup = BeautifulSoup(res.text, "lxml")
                    price_now = int(soup.find("p", attrs={"class":"no_today"}).find("span", attrs={"class":"blind"}).get_text().replace(",",""))
                    updown = (price_now - int(line[3]))/float(int(line[3]))
                    
                    line.extend([price_now, updown])
                    writer.writerow(line)

def saveCSV_20(): # 중기
    li = sorted(os.listdir(f"{path}10\\"))
    if len(li) >= 10:
        with open(f"{path}\\10\\{li[len(li)-10]}", "r", encoding="utf-8-sig") as f:
            with open(f"{path}\\20\\{li[len(li)-10][:-4]}_20.csv", "w", encoding="utf-8-sig", newline="") as f_w:
                reader = csv.reader(f)
                writer = csv.writer(f_w)
                for line in reader:
                    del line[-1]
                    url = default_link + line[2]
                    res = requests.get(url)
                    soup = BeautifulSoup(res.text, "lxml")
                    price_now = int(soup.find("p", attrs={"class":"no_today"}).find("span", attrs={"class":"blind"}).get_text().replace(",",""))
                    updown = (price_now - int(line[3]))/float(int(line[3]))
                    
                    line.extend([price_now, updown])
                    writer.writerow(line)

def saveCSV_60(): # 중장기
    li = sorted(os.listdir(f"{path}20\\"))
    if len(li) >= 40:
        with open(f"{path}\\20\\{li[len(li)-40]}", "r", encoding="utf-8-sig") as f:
            with open(f"{path}\\60\\{li[len(li)-40][:-4]}_60.csv", "w", encoding="utf-8-sig", newline="") as f_w:
                reader = csv.reader(f)
                writer = csv.writer(f_w)
                for line in reader:
                    del line[-1]
                    url = default_link + line[2]
                    res = requests.get(url)
                    soup = BeautifulSoup(res.text, "lxml")
                    price_now = int(soup.find("p", attrs={"class":"no_today"}).find("span", attrs={"class":"blind"}).get_text().replace(",",""))
                    updown = (price_now - int(line[3]))/float(int(line[3]))
                    
                    line.extend([price_now, updown])
                    writer.writerow(line)

def saveCSV_120(): # 장기
    li = sorted(os.listdir(f"{path}60\\"))
    if len(li) >= 60:
        with open(f"{path}\\60\\{li[len(li)-40]}", "r", encoding="utf-8-sig") as f:
            with open(f"{path}\\120\\{li[len(li)-40][:-4]}_120.csv", "w", encoding="utf-8-sig", newline="") as f_w:
                reader = csv.reader(f)
                writer = csv.writer(f_w)
                for line in reader:
                    del line[-1]
                    url = default_link + line[2]
                    res = requests.get(url)
                    soup = BeautifulSoup(res.text, "lxml")
                    price_now = int(soup.find("p", attrs={"class":"no_today"}).find("span", attrs={"class":"blind"}).get_text().replace(",",""))
                    updown = (price_now - int(line[3]))/float(int(line[3]))
                    
                    line.extend([price_now, updown])
                    writer.writerow(line)

# 테스트용
if __name__ == "__main__":
    saveCSV_5()
    saveCSV_10()
    saveCSV_20()
    saveCSV_60()
    saveCSV_120()