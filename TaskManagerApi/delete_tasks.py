from .models import Task
from .database import SessionLocal

db=SessionLocal()

Tasks=db.query(Task).filter(Task.id==2).first()

if Tasks:
    db.delete(Tasks)
    db.commit()

db.close()