from django.db import models

class ToDoItem(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=1, choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])

    def __str__(self):
        return self.text
