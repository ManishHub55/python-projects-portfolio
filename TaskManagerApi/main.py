from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from .database import get_db
from .models import Task

app=FastAPI()

#Get all
@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

#get one
@app.get("/tasks/{id}")
def get_tasks(id:int,db: Session = Depends(get_db)):
    rows=db.query(Task).filter(Task.id==id).first()
    if rows:
        return rows

#create
@app.post("/tasks")
def create_tasks(title:str,db: Session = Depends(get_db)):
    new_task=Task(title=title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

#update
@app.put("/tasks/{id}")
def update_task(id:int,new_title:str,db:Session=Depends(get_db)):
    task=db.query(Task).filter(Task.id==id).first()

    if task:
         task.id=id
         task.title=new_title
         db.commit()
         db.refresh(task)
         return {"Message":f"task {id} is  successfully updated."}
    else:
        return {"Error":"task not found"}
    
#delete
@app.delete("/tasks/{id}")
def delete_task(id:int,db:Session=Depends(get_db)):
    task=db.query(Task).filter(Task.id==id).first()

    if task:
        db.delete(task)
        db.commit()
        return {"Message":f"task {id} is successfully deleted."}
    else:
        return {"Error":"task not found"}