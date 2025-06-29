from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_id = models.FloatField(max_length=50)
    mobile = models.CharField(max_length=12)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

