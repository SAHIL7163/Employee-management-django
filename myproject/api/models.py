from django.db import models

# Create your models here.
class Department(models.Model):
    department_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.name
    

#Employee Model
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
