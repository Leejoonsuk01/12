def kiosk_menu():
    menu = ["냉면", "볶음밥", "피자", "짜장면"]
    while True:
        try:
            food = int(input("메뉴를 선택하세요 (1: 돈까스, 2: 제육, 3: 미네랄워터, 4: 짜장면): "))
            if food < 1 or food > 4:
                raise IndexError
            print(f"선택하신 메뉴는 {menu[food - 1]}입니다.")
            break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
        except IndexError:
            print("잘못된 번호입니다. 1~4 사이 숫자를 입력해주세요.")

kiosk_menu()