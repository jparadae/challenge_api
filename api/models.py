from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)

class Job(models.Model):
    title = models.CharField(max_length=255)

class Employee(models.Model):
    name = models.CharField(max_length=255)
    hire_date = models.DateField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)  # Clave foránea
    job = models.ForeignKey('Job', on_delete=models.CASCADE)  # Clave foránea
