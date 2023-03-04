from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import Field, EmailStr
from .user_model import User

class Question(Document):
    question_id: UUID = Field(default_factory=uuid4, unique = True)
    titre: str
    reponse : bool
    description: str
    created_at : datetime = Field(default_factory=datetime.utcnow)
    updated_at : datetime = Field(default_factory=datetime.utcnow)
    user_id : UUID
    owner : Link[User]

    def __repr__(self) -> str:
        return f"<Question {self.titre}>"

    def __str__(self) -> str:
        return self.titre

    def __hash__(self) -> int:
        return hash(self.titre)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Question):
            return self.question_id == other.question_id
        return False
    
    @before_event([Replace, Insert])
    def update_update_at(self):
        self.updated_at= datetime.utcnow()

    class Collection:
        name = "questions"    
