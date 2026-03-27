import json
import os
file_path="data/students.json"

def load_students():
    try:
        with open(file_path,"r") as f:
            return json.load(f)
    except:
        return []

def save_students(student):
    
    with open(file_path,"w") as f:
        json.dump(student,f,indent=4)



