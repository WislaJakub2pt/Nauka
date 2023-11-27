from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_lensgth=20)

    def __string__(self):
        return self.username    