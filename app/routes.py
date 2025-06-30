from fastapi import APIRouter, HTTPException, Depends, Query
from sqlmodel import Session, select
from typing import List
from .models import Task
from .schemas import TaskCreate, TaskUpdate, TaskResponse
from .database import get_session

router = APIRouter()

@router.get("/", tags=["Info"])
def root():
    return {"message": "Task Management API", "endpoints": ["/tasks", "/health", "..."]}

@router.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}

@router.post("/tasks", response_model=TaskResponse, status_code=201, tags=["Tasks"])
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    db_task = Task(**task.dict())
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.get("/tasks", response_model=List[TaskResponse], tags=["Tasks"])
def list_tasks(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    tasks = session.exec(select(Task).offset(skip).limit(limit)).all()
    return tasks

@router.get("/tasks/{task_id}", response_model=TaskResponse, tags=["Tasks"])
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=TaskResponse, tags=["Tasks"])
def update_task(task_id: int, update_data: TaskUpdate, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(task, key, value)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.delete("/tasks/{task_id}", status_code=204, tags=["Tasks"])
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return

@router.get("/tasks/status/{status}", response_model=List[TaskResponse], tags=["Tasks"])
def filter_by_status(status: str, session: Session = Depends(get_session)):
    tasks = session.exec(select(Task).where(Task.status == status)).all()
    return tasks

@router.get("/tasks/priority/{priority}", response_model=List[TaskResponse], tags=["Tasks"])
def filter_by_priority(priority: str, session: Session = Depends(get_session)):
    tasks = session.exec(select(Task).where(Task.priority == priority)).all()
    return tasks
