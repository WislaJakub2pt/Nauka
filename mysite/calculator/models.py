from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __string__(self):
        return f"{self.username} - {self.id}"   
        