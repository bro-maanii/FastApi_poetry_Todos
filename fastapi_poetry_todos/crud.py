from sqlalchemy.orm import Session
from .models import *
from .schemas import *

# single todo
def get_todo(db: Session, todo_id: int):
    return db.query(Todos).filter(Todos.id == todo_id).first()

# all todos
def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todos).offset(skip).limit(limit).all()

# create todo
def create_todo(db: Session, todo: TodoBase):
    db_todo = Todos(title=todo.title, description = todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return "successfully created"

# delete todo
def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(Todos).filter(Todos.id == todo_id).first()
    db.delete(db_todo)
    db.commit()
    return "deleted"

# update todo text
def update_todo(db: Session, todo_id: int, todo:TodoBase):
    db_todo = db.query(Todos).filter(Todos.id == todo_id).first()
    db_todo.title = todo.title
    db_todo.description = todo.description
    db.commit()
    db.refresh(db_todo)
    return "updated"