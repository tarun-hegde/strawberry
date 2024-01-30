from todo.models import TodoItem
import strawberry
from typing import List
from .types import TodoItemType
# Create Read Schema
@strawberry.type
class Query:
    @strawberry.field
    def tasks(self) -> List[TodoItemType]:
        return TodoItem.objects.all()
    
@strawberry.type
class Mutation:
    @strawberry.field
    def create_task(self, content: str, author: str) -> TodoItemType:
        return TodoItem.objects.create(content=content, author=author)
    
    @strawberry.field
    def delete_task(self, id: int) -> bool:
        TodoItem.objects.get(id=id).delete()
        return True
    
    @strawberry.field
    def update_task(self, id: int, content: str, author: str) -> TodoItemType:
        task = TodoItem.objects.get(id=id)
        task.content = content
        task.author = author
        task.save()
        return task
    
schema = strawberry.Schema(query=Query, mutation=Mutation)
