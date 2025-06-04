from budget import Budget
import math

def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 하루 점검")
        print("5. 주택담보대출 계산기")
        print("6. 종료")
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
            # 주택담보대출 계산기: 원리금균등상환방식
            try:
                principal = float(input("대출 원금을 입력하세요(원): "))
                annual_rate = float(input("연 이자율을 입력하세요(%, 예: 3.5): "))
                years = int(input("대출 기간을 입력하세요(년): "))
            except ValueError:
                print("잘못된 입력입니다.\n")
                continue
            r = annual_rate / 100 / 12  # 월 이자율
            n = years * 12  # 총 납입 개월 수
            if r == 0:
                monthly_payment = principal / n
            else:
                monthly_payment = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
            total_payment = monthly_payment * n
            total_interest = total_payment - principal
            print(f"월 납입금: {math.ceil(monthly_payment):.0f}원")
            print(f"총 납입액: {math.ceil(total_payment):.0f}원 (이자 포함)")
            print(f"총 이자 비용: {math.ceil(total_interest):.0f}원\n")

        elif choice == "6":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")

if __name__ == "__main__":
    main()
