from django.db import models

# Class to represent an employee and their releveant fields
class Employee(models.Model):
    TCC_ID = models.IntegerField()
    name = models.CharField(max_length=15)
    score = models.IntegerField()
    is_keyholder = models.BooleanField(default=False)
    is_newbie = models.BooleanField(default=False)
    is_espresso = models.BooleanField(default=False)
    is_AM = models.BooleanField(default=False)
    # TODO add MOCA constraints

#foo = Employee.objects.create(name="michael", score=7)
