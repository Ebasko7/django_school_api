from django.db import models
from .validators import validate_name_format, validate_school_email, validate_combination_format, validate_locker_number, validate_personal_email

class Student(models.Model):
    name = models.CharField(validators=[validate_name_format])
    student_email = models.EmailField(unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(blank=True, unique=True, validators=[validate_personal_email]''')
    locker_number = models.IntegerField(default=110, unique=True, validators = [validate_locker_number])
    locker_combination = models.CharField(unique=False, default = '12-12-12', validators=[validate_combination_format])
    good_student = models.BooleanField(default=True)

    def __str__(self):
        return f'Student Name:{self.name} Student Email: {self.student_email} Student Locker: {self.locker_number}'

    def locker_reassignment(self, new_locker):
        self.locker_number = new_locker
        self.save()
    
    def student_status(self, is_good_student):
        self.good_student = is_good_student
        self.save()

