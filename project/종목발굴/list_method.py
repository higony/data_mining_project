# 1.1.0 : 종목 정보가 포함된 list를 다루는 메소드 모음.
def read_list(li):
    # li 안의 각 요소들의 형태 : (종목명, 현재가, 거래량)
    length = len(li)
    print(f"총 {length}개의 검색 결과가 있습니다.")
    for i in range(length):
        print(f"{i+1}. {li[i][0]}")
        print(f"현재가 {li[i][1]}원\t거래량 {li[i][2]}")
        print("-"*100)