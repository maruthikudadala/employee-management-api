from django.db import models
from django.core.validators import EmailValidator

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    department = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"