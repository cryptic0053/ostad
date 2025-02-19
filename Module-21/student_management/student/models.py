from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    checkbox = models.BooleanField

    def __str__(self):
        return f"{self.name}"
