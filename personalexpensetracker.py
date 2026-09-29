expenses={}
def add_expense():
    while True:
        expense=input("Enter the name of expense: ").lower()
        amount=input("Enter the amount: ")
        if amount.isdigit():
            amount=int(amount)
            expenses[expense]=amount
            print("Expense added!")
            break
        else:
            print("Enter a valid amount!")
def view_expenses():
    if expenses=={}:
        print("Empty!\nAdd Expenses to see.")
    else:
        print(', '.join(f"{k}: {v}" for k,v in expenses.items()))

def total_spent():
    total=[]
    if expenses=={}:
        print("Nothing added in expenses!")
    else:
        for i in expenses:
            total.append(expenses[i])
            totalsp=sum(total)
        print(f"Total Spent: {totalsp}")


def highest_expense():
    highestex=""
    highestmoney=0
    for i in expenses:
        if highestmoney<expenses[i]:
            highestmoney=expenses[i]
            highestex=i
    print(f"Highest Expense: {highestex}\nAmount: {highestmoney}")


def delete_expense():
    delete=input("Which one you want to delete?: ")
    if delete.lower() in expenses:
        expenses.pop(delete.lower())
        print(f"{delete} deleted successfully!")
    else:
        print("Expense not found!")

def main():
    while True:
        print("1.Add Expenses\n" \
        "2.View Expenses\n" \
        "3.Total Spent\n" \
        "4.Highest Expense\n" \
        "5.Delete Expenses\n" \
        "6.Exit")
        while True:
            user=input("Choose any option(1-6): ")
            if user.isdigit():
                user=int(user)
                if 1<=user<=6:
                     break
                else:
                    print("Enter between(1-6)!")
            else:
                print("Invalid Typing!\nTry again.")
        if user==1:
            add_expense()
        elif user==2:
            view_expenses()
        elif user==3:
            total_spent()
        elif user==4:
            highest_expense()
        elif user==5:
            delete_expense()
        elif user==6:
            break
main()