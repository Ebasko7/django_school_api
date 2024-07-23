from django.db import models
from .validator import validate_name_format

class Student(models.Model):
    name = models.CharField(validators = [validate_name_format])
    student_email = models.EmailField(unique=True)
    personal_email = models.EmailField(blank=True, unique=True)
    locker_number = models.IntegerField(default=110, unique=True)
    locker_combination = models.CharField(unique=False, default = '12-12-12')
    good_student = models.BooleanField(default=True)

    def __str__(self):
        return f'Student Name:{self.name} Student Email: {self.student_email} Student Locker: {self.locker_number}'

    def locker_reassignment(self, new_locker):
        self.locker_number = new_locker
        self.save()
    
    def student_status(self, is_good_student):
        self.good_student = is_good_student
        self.save()

