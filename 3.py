class Beverage:
    menu = {"커피": 3000, "녹차": 2500, "아이스티": 3000}

    def __init__(self, name):
        if name in Beverage.menu:
            self.name = name
            self.price = Beverage.menu[name]
        else:
            raise ValueError(f"{name}은(는) 메뉴에 없는 음료입니다. 메뉴에서 선택해주세요.")

    def calculate_total_price(self, quantity):
        if quantity > 0:
            return self.price * quantity
        else:
            raise ValueError("수량은 0보다 커야 합니다.")

def take_order():
    print("메뉴:")
    for name, price in Beverage.menu.items():
        print(f"{name}: {price}원")

    try:
        choice = input("음료를 선택하세요 (커피, 녹차, 아이스티): ")
        beverage = Beverage(choice)  # 음료 객체 생성
        quantity = int(input("수량을 입력하세요: "))
        total_price = beverage.calculate_total_price(quantity)
        print(f"{beverage.name} {quantity}잔의 총 가격은 {total_price}원입니다.")
    except ValueError as e:
        print(e)

# 사용 예
take_order()