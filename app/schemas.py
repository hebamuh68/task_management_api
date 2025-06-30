from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

from app.utils import TitleValidationMixin, TaskBase


class TaskCreate(TitleValidationMixin, TaskBase):
    title: str

    @validator("due_date")
    def due_date_must_be_future(cls, v):
        if v and v <= datetime.utcnow():
            raise ValueError("Due date must be in the future.")
        return v


class TaskUpdate(TitleValidationMixin, TaskBase):
    title: Optional[str]


class TaskResponse(TaskCreate):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
