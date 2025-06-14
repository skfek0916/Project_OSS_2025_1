from budget import Budget

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 하루 점검")
        print("5. 종료")
        choice = input("선택 > ")

        if choice == "1":
            print("1. 교통비 / 2. 기타")
            sub = input("지출 유형 선택 > ")
            if sub == "1":
                budget.add_transport_expense()
            else:
                category = input("카테고리 (예: 식비, 생활용품 등): ")
                description = input("설명: ")
                try:
                    amount = int(input("금액(원): "))
                except ValueError:
                    print("잘못된 금액입니다.\n")
                    continue
                budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            budget.daily_check()

        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()