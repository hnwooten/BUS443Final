from django.db import models

# Create your models here.


class CourseDetails(models.Model):
    courseid = models.IntegerField()
    coursetitle = models.CharField(max_length=500)
    coursename = models.CharField(max_length=500)
    coursesectioncode = models.IntegerField()
    coursedepartment = models.CharField(max_length=500)
    courseinstructor = models.CharField(max_length=500)
    
    
class StudentDetails(models.Model):
    studentid = models.IntegerField()
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    major = models.CharField(max_length=500)
    year = models.CharField(max_length=500)
    gpa = models.CharField(max_length=500)