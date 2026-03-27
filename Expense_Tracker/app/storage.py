import json
import sys
FILE_PATH="data/expenses.json"

#Read expense from json
def load_expenses():
      try:
            with open(FILE_PATH,"r") as f:
                  return json.load(f)
      except FileNotFoundError:
            print("Check File Path.")
            sys.exit()
      except Exception:
            return []

#write expense in json
def save_expenses(expense):
        with open(FILE_PATH,"w") as f:
            json.dump(expense,f,indent=4)

