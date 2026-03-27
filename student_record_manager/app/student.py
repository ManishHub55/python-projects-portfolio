class Student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    
    def show_record(self):
        return {"id":self.id,"name":self.name,"age":self.age}
