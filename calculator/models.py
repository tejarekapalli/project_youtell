from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Calculation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    operation = models.CharField(max_length=10)
    left_operand = models.IntegerField()
    right_operand = models.IntegerField()
    result = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Master(AbstractUser):
    pass

class Student(AbstractUser):
    pass

