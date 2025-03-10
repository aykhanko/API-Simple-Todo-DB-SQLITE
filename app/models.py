from django.db import models
from django.contrib.auth.models import User

class Todos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    todo = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta():
        verbose_name_plural = 'TODOS'