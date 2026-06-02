from .models import Task
from .database import SessionLocal

db=SessionLocal()

Task_list=db.query(Task).all()

for t in Task_list:
    print(f"id:{t.id} title:{t.title}")