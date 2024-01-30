import strawberry
from .models import TodoItem

@strawberry.django.type(TodoItem)

class TodoItemType:
    id: int
    content: str
    author: str