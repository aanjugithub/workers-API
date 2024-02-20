from django.db import models

# Create your models here.

class Employees(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    dob=models.DateField(blank=True, null=True)
    phone_number=models.CharField(max_length=15, blank=True, null=True)
    designation=models.CharField(max_length=100)
    salary=models.PositiveIntegerField()

    def __str__(self):
        return self.name
