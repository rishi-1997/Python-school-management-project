from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    is_principal = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Principal(models.Model):
    user = models.ForeignKey('app_SMP.User', on_delete=models.CASCADE)


class Student(models.Model):
    user = models.ForeignKey('app_SMP.User', on_delete=models.CASCADE)


class Teacher(models.Model):
    user = models.ForeignKey('app_SMP.User', on_delete=models.CASCADE)


class Teacher_List(models.Model):
    Username = models.CharField(max_length=20, unique=True, primary_key=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Joining_date = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)
    address = models.CharField(max_length=100)


class Student_List(models.Model):
    Username = models.CharField(max_length=20, unique=True, primary_key=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Joining_date = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)
    address = models.CharField(max_length=100)


class Student_Result(models.Model):
    Username = models.CharField(max_length=20, unique=True, primary_key=True)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField()
    social_studies = models.IntegerField()
    english = models.IntegerField()
    hindi = models.IntegerField()


class students_attendance(models.Model):
    Username = models.ForeignKey(Student_List, on_delete=models.CASCADE)
    ATTENDANCE_CHOICE = (
        ('P', 'Present'),
        ('A', 'Absent'),
    )
    Attendance_status = models.CharField(max_length=1, choices=ATTENDANCE_CHOICE)
    Reason = models.CharField(max_length=50,null=True, blank=True)
    attendance_date = models.DateField()
