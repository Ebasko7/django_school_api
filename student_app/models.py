from django.db import models

class Student(models.Model):
    name = models.CharField()
    student_email = models.EmailField()
    personal_email = models.EmailField()
    locker_number = models.IntegerField()
    locker_combination = models.CharField()
    good_student = models.BooleanField()

