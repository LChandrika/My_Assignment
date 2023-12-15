from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(max_length=100)
    empsalary = models.FloatField()

    def __str__(self):
        return f"{self.empid}--{self.empname}"
    

