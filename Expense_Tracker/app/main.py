from .expense import Expense
from .storage import save_expenses,load_expenses

#Add Expense
def add_expense():
    category=input("Enter Expense Category: ")
    amount=input("Enter Expense Amount: ")
    expense=Expense(category,amount)
    expense_data=expense.show_expense()
    expense_list=load_expenses()
    expense_list.append(expense_data)
    save_expenses(expense_list)


#View Expense
def view_expenses():
   expenses= load_expenses()
   for e in expenses:
       print(e)


#Filter Expense
def filter_expense():
    category=input("Enter Filter Category: ")
    expense_list= load_expenses()
    new_list=[]
    for e in expense_list:
        if e["category"]==category:
            new_list.append(e)

    return new_list


def filter_expenses():
    new_list=filter_expense()
    [print(e) for e in new_list]


#Total Expense(Category-Wise)
def total_expense_Category_wise():
    new_list=filter_expense()
    total=0
    for e in new_list:
        if e["amount"]!=None:
            total=total+int(e["amount"])
    print(f"Total Expense(Category-Wise):={total}")


#Total Expense(ALL)
def total_expense_All():
    expenses_list=load_expenses()
    total=0
    for e in expenses_list:
        total=total+int(e["amount"])
    print(f"Total Expense(ALL):{total}")



#main()

def main():
    while True:
        print("=====Expense Tracker(CLI APP)=====")
        print("\n 1.Add Expense.")
        print("\n 2.View Expenses.")
        print("\n 3.Filter Expenses.")
        print("\n 4.Total Expense(Category-Wise).")
        print("\n 5.Total Expense(ALL).")
        print("\n 6.Exit.")

        choice= input("\n Enter Your Choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            total_expense_Category_wise()
        elif choice == "5":
            total_expense_All()
        elif choice == "6":
            break
        else:
            print("Invalid Choice.")
            
#condition
if __name__=="__main__":
        main()