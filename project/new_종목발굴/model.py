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
