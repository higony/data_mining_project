# 1.1.0 : main 함수 내에서 동작하는 메소드로 정의
# 1.1.1 : 리스트를 통하여 스크래핑 진행.
def stock_list_by_price(li):
    try: # 1.0.2 : 원하는 가격대의 종목을 확인할 수 있도록 하는 기능 구현 + 예외 처리
        minimum_price = int(input("조회를 원하는 종목의 최소 가격을 입력해주세요: "))
        maximum_price = int(input("조회를 원하는 종목의 최대 가격을 입력해주세요: "))
        result = []
        for element in li: # 필요한 정보 : 가격. index num 1
            # 종목명은 1번째, 현재가는 2번째, 거래량은 9번째 요소.
            if element[1] not in range(minimum_price, maximum_price+1): # 주가가 원하는 범위 내가 아니라면,
                continue
            result.append(element)
        print("검색을 종료합니다. ", end="")
        print(f"총 {len(result)}개의 검색 결과가 있습니다.")
        return result
    except:
        print("오류가 발생했습니다.")
        