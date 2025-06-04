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
            # K패스 교통카드는 20% 할인 적용
            discounted = int(amount * 0.8)
            expense = Expense(today, "교통비", "K패스 교통카드", discounted)
            print(f"할인 전 금액: {amount}원, 할인 후 저장된 금액: {discounted}원")
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