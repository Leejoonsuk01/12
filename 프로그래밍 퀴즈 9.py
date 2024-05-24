class 붕어빵:
    total_sales = 0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.total = 0

    def sell(self):
        print(f"{self.name} 붕어빵이 판매되었습니다. 가격 = {self.price}원")
        self.total += self.price

    def total(self):
        print(f"총 판매금: {붕어빵.total}원")
        print(f"{self.name} 붕어빵 총 판매금: {self.total}원")

크림_붕어빵=붕어빵(name="슈크림", price=2000)


크림_붕어빵.sell()
크림_붕어빵.sell()

print("누적 판매금액은",크림_붕어빵.total,"입니다" )
