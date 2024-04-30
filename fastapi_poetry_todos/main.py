from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from .models import *
from .schemas import *
from .crud import *
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/todos")
def create_todo_task(todo: TodoBase, db: Session = Depends(get_db)):
    return create_todo(db=db, todo=todo)

@app.get("/api/todos")
def get_todos_task(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = get_todos(db, skip=skip, limit=limit)
    return todos

@app.delete("/api/todos/{todo_id}")
def delete_todo_task(todo_id: int, db: Session = Depends(get_db)):
    return delete_todo(db, todo_id=todo_id)

@app.put("/api/todos/{todo_id}")
def update_todo_task(todo_id: int, todo: TodoBase, db: Session = Depends(get_db)):
    return update_todo(db, todo_id=todo_id, todo=todo)


