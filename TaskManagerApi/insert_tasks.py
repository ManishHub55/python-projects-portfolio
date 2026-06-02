from .database import SessionLocal 
from .models import Task

db=SessionLocal()

new_task=Task(title="Learn FastAPI")

db.add(new_task)

db.commit()

db.close()
