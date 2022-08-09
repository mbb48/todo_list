from django.db import models

class Todo(models.Model):
    todo=models.CharField(max_length=100)
    is_complate=models.IntegerField()
    create_date=models.DateTimeField()

    def __str__(self):
        return self.todo