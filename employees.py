import mysql.connector
from django.db import models

connection = mysql.connector.connect(user='root', host='localhost', port='3306', password='thenagain')
myquery = connection.cursor()

results = None
for q in myquery:
    results += q

# Class to represent an employee and their releveant fields
#class Employee(models.Model):
#    name = models.CharField(max_length=15)
#    score = models.IntegerField() # 1 = worst; 10 = best
#    is_keyholder = models.BooleanField(default=False)
#    is_newbie = models.BooleanField(default=False)
#    is_espresso = models.BooleanField(default=False)
#    is_AM = models.BooleanField(default=False)
#    # TODO add MOCA constraints

#foo = Employee.objects.create(name="michael", score=7)
