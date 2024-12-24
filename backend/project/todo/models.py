from django.db import models
from users.models import Account
class ToDoItem(models.Model):

    author = models.ForeignKey(Account, on_delete=models.CASCADE, default='')
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=1, choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])

    def __str__(self):
        return self.text
