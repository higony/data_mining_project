class stock:
    def __init__(self, name, price, updown, amount, link):
        self.name = name
        self.price = price
        self.updown = updown
        self.amount = amount
        self.link = link

    def print(self):
        print(f"{self.name} : {self.link}")
        print(f"현재가 {self.price} ({self.updown}%) / 거래량 {self.amount}\n")

    # 1.0.1 외인/기관 연속 순매수일 담는 정보 입력하기
    def input_purchase(self, p_tuple):
        self.purchase = p_tuple