expenses=[]
def add_expenses(expenses):
   name=input("enter expenses name:")
   amount=int(input("enter the amount of expenses"))
   expenses.append({"name":name,"amount":amount})
   print("expenses added")
   print(f"expenses added: {expenses}")  # ✅
# enumerate() dono cheez ek saath deta hai — index aur value.
# i → index (number)
# exp → us number pe jo value hai

def show_expenses(expenses):
      for i , exp in enumerate(expenses):
           print(f"{i+1}. {exp['name']} ,{exp['amount']}")
add_expenses(expenses)
show_expenses(expenses) 
total=0
def total_expenses(expenses):
    total = 0
    for exp in expenses:
        total = total + exp["amount"]
    print("Total Expense: ₹", total)
