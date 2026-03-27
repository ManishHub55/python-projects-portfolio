class Expense:
    def __init__(self,category,amount):
        self.amount=amount
        self.category=category
    
    def show_expense(self):
        return {"category":self.category,"amount":self.amount}
    
