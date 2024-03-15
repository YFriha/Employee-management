from django.db import models

class Departements(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName= models.TextField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName= models.TextField(max_length=500)
    Department=models.CharField(max_length=500)
    DateOfJoining= models.DateField()
    PhotoFileName= models.CharField(max_length=500)