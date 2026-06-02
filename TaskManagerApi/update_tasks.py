from .database import SessionLocal
from .models import Task

db=SessionLocal()

rows=db.query(Task).filter(Task.id==2).first()

if rows:
    rows.title="LEARN REAL CRUD SYSTEM"
    db.commit()

db.close()