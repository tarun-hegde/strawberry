from django.db import models

# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=50)
    def __str__(self):
        return self.content