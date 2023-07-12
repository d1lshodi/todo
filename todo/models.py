from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class TodoModel(models.Model):
    task = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
 

    def __str__(self):
        return self.task
    
    class Meta:
        db_table = "todo"
