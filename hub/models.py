from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.

class User(AbstractUser):
    groups = models.ManyToManyField(
        'self',
      help_text='The groups this user belongs to.',)
    
    user_permissions = models.ManyToManyField('self',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',)
    
    def __str__(self):
       return self.username
    
    
class Course(models.Model):
    subject = models.CharField(max_length=128, null=True)
    code = models.CharField(max_length=8, null=True)
    level = models.CharField(max_length=128, null=True)
    professor = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,related_name="professor")
    students = models.ManyToManyField(User, symmetrical= False,blank=True)
    program = models.CharField(max_length=1028,null=True,blank=True)

    def __str__(self):
        return self.subject
    
class Forum(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="commentCreator")
    content = models.CharField(max_length=512, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,blank=True,null=True,related_name="forumCourse")
    
    def __str__(self):
        return f"{self.creator}: {self.course}"
    
class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="creator")
    title = content = models.CharField(max_length=512, null=True)
    content = models.CharField(max_length=512, null=True)
    timestamp = models.DateTimeField(auto_now=timezone.now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,blank=True,null=True,related_name="coursePost")
    filec = models.FileField(upload_to='uploads/', null=True, blank=True)
    assignment = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.creator}: {self.course}({self.id})"
    
class Assignment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, blank=True, null=True, related_name="post")
    student = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="studentAssignment")
    grade = grade = models.FloatField(max_length=4, null=True)
    filec = models.FileField(upload_to='uploads/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=timezone.now)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,blank=True,null=True,related_name="assingmentPost")
    
    def __str__(self):
        return f"student:{self.student} - {self.post}"
    
class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,related_name="studentGrade")
    course=  models.ForeignKey(Course, on_delete=models.CASCADE,blank=True,null=True,related_name="courseGrade")
    grade = models.FloatField(max_length=4, null=True)
    is_failed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.course.subject} - {self.student}"