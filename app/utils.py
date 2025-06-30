from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator

from app.models import TaskStatus, TaskPriority


class TitleValidationMixin:
    @validator("title")
    def title_cannot_be_blank(cls, v):
        if v is not None and not v.strip():
            raise ValueError("Title cannot be empty or whitespace.")
        return v.strip() if v else v

class TaskBase(BaseModel):
    description: Optional[str]
    status: Optional[TaskStatus]
    priority: Optional[TaskPriority]
    due_date: Optional[datetime]
    assigned_to: Optional[str]
