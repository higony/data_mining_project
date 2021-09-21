class stock:
    def __init__(self, name, price, updown, amount, link):
        self.name = name
        self.price = price
        self.updown = updown
        self.amount = amount
        self.link = link
        
        # 1.0.2 종목코드 추가 -> 검색을 용이하게 하기 위함
        self.code = link[-6:]

        # 1.0.2 연속 순매수일 관련 특이사항 저장
        """
        외인/기관 3일 연속 매수 + 외인 5일 연속 매수 -> 외인 주도 쌍끌이 매수세 포착
        외인/기관 3일 연속 매수 + 기관 5일 연속 매수 -> 기관 주도 쌍끌이 매수세 포착
        외인/기관 5일 연속 매수 -> 강한 쌍끌이 매수세 포착
        """
        self.comment = ""

    def print(self):
        print(f"{self.name}({self.code}) : {self.link}")
        print(f"현재가 {self.price} ({self.updown}%) / 거래량 {self.amount}")
        if self.comment != "":
            print(self.comment, "\n")
        

    # 1.0.1 외인/기관 연속 순매수일 담는 정보 입력하기
    def input_purchase(self, p_tuple):
        self.purchase = p_tuple