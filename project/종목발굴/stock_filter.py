# 1.1.0 : main 함수 내에서 동작하는 메소드로 정의.
# 1.1.1 : 리스트를 통하여 스크래핑 진행.
# 1.1.2 : 거래량 기준 필터 기능 추가

def finalize(li):
    print("검색을 종료합니다. ", end="")
    print(f"총 {len(li)}개의 검색 결과가 있습니다.")

def stock_list_by_price(li):
# 1.0.2 : 원하는 가격대의 종목을 확인할 수 있도록 하는 기능 구현 + 예외 처리
# 1.1.2 : 메소드 영역에서 예외 처리 기능 삭제
    minimum_price = int(input("조회를 원하는 종목의 최소 가격을 입력해주세요: "))
    maximum_price = int(input("조회를 원하는 종목의 최대 가격을 입력해주세요: "))
    result = []
    for element in li: # 필요한 정보 : 가격. index num 1
        if element[1] not in range(minimum_price, maximum_price+1): # 주가가 원하는 범위 내가 아니라면,
            continue
        result.append(element)
    finalize(result)
    return result

def stock_list_by_amount(li):
    minimum_amount = int(input("조회를 원하는 종목의 최소 거래량을 입력해주세요: "))
    maximum_amount = input("조회를 원하는 종목의 최대 거래량을 입력해주세요. 설정을 원하지 않으시다면 엔터키를 눌러주세요: ")
    # 필요한 정보: 거래량. index num 3
    if maximum_amount == "":
        ifs = 1
    else:
        maximum_amount = int(maximum_amount)
        ifs = 2
    
    result = []
    for element in li:
        if ifs == 1 and element[3] < minimum_amount:
            continue
        elif ifs == 2 and element[3] not in range(minimum_amount, maximum_amount+1):
            continue
        result.append(element)
    finalize(result)
    return result