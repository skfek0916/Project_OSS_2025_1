import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def add_transport_expense(self):
        today = datetime.date.today().isoformat()
        # K패스 교통카드 여부 선택
        sub_choice = input("1. K패스 교통카드 / 2. 기타 교통수단 > ")

        try:
            amount = int(input("금액(원): "))
        except ValueError:
            print("잘못된 금액입니다.\n")
            return

        if sub_choice == "1":
            # K패스 교통카드 사용자 타입 선택
            print("1. 일반인 (20% 할인) / 2. 청소년층 (30% 할인) / 3. 저소득층 (53% 할인)")
            user_type = input("사용자 유형 선택 > ")

            if user_type == "1":
                rate = 0.8
                type_desc = "일반인"
            elif user_type == "2":
                rate = 0.7
                type_desc = "청소년층"
            elif user_type == "3":
                rate = 0.47
                type_desc = "저소득층"
            else:
                print("잘못된 선택입니다. 일반인 기준 할인 적용합니다.")
                rate = 0.8
                type_desc = "일반인"

            discounted = int(amount * rate)
            description = f"K패스 교통카드 ({type_desc})"
            expense = Expense(today, "교통비", description, discounted)
            print(f"할인 전 금액: {amount}원, 할인율: {(1-rate)*100:.0f}%, 할인 후 저장된 금액: {discounted}원")
        else:
            expense = Expense(today, "교통비", "기타 교통수단", amount)

        self.expenses.append(expense)
        print("교통비가 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

