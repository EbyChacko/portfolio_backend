from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.message}'