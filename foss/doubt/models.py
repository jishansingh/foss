from django.db import models
from .choices import CHOICE
from django.contrib.auth.models import User

# Create your models here.

class Reply(models.Model):
    content=models.TextField()
    anonymous=models.BooleanField(default=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Question(models.Model):
    question=models.CharField(max_length=30)
    content=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='by_user')
    category=models.CharField(choices=CHOICE,max_length=30)
    likes=models.IntegerField(default=0)
    visited=models.ManyToManyField(User,blank=True,related_name='visited_users')
    reply=models.ManyToManyField(Reply)

class UserProfile(models.Model):
    user=models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    photo=models.ImageField()
    email=models.EmailField()
    roll_no=models.CharField(max_length=20,default="")
    my_question=models.ManyToManyField(Question,blank=True,related_name='asked_question')
    dislike=models.ManyToManyField(Question,blank=True,related_name='disliked')
    liked=models.ManyToManyField(Question,blank=True,related_name='liked_ques')
    visited=models.ManyToManyField(Question,blank=True,related_name='visited_ques')







