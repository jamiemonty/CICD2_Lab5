from typing import Annotated
from pydantic import BaseModel, EmailStr, Field, StringConstraints, ConfigDict

studentId = Annotated[str, StringConstraints(pattern = r'^S\d{7}$')]

class UserCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str | None = None
    student_id: studentId

class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    email: EmailStr
    full_name: str | None = None
    student_id: studentId