from .student import Student
from .storage import load_students,save_students

def add_students():
    id=input("Enter Student Id: ")
    name=input("Enter Student Name: ")
    age=input("Enter Student Age: ")
    student=Student(id,name,age)
    record=student.show_record()
    students=load_students()
    students.append(record)
    save_students(students)

def view_students():
   students=load_students()
   for s in students:
       print(s)

def search_students():
    id=input("Enter Student Id: ")
    students=load_students()
    for s in students:
        if s["id"]==id:
            return s
    return "Id Not Found."

def delete_students():
    id=input("Enter Student Id: ")
    students=load_students()
    updated_students=[]
    updated_students=[s for s in students if s["id"]!=id]

    if len(updated_students)==len(students):
        print("Student Not Existed.")
    else:
        save_students(updated_students)
        print("Student Deleted.")


def main():
    while(True):
      print("=====Student Recored Manager=====\n")
      print("\n1. Add Student")  
      print("\n2. View Student")  
      print("\n3. Search Student")  
      print("\n4. Delete Student")  
      print("\n5. Exit.")  
      
      choice= input("\n Enter Your Choice: ")
      if choice == "1":
          add_students()
      elif choice == "2":
          view_students()
      elif choice == "3":
          print(search_students())
      elif choice == "4":
          delete_students()
      elif choice == "5":
          break
      else:
          print("Invalid Choice.")
          

if __name__=="__main__":
    main()