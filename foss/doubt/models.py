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
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(choices=CHOICE,max_length=30)
    likes=models.IntgerField(default=0)
    visited=models.ManyToManyField(User,null=True)
    reply=models.ManyToManyField(Reply)

class UserProfile(models.Model):
    user=models.OneToOneField(User,related_name='user_profile')
    photo=models.ImageField()
    email=models.EmailField()
    roll_no=models.CharField(max_length=20)
    my_question=models.ManyToManyField(question,null=True,related_name='my_question')
    dislike=models.ManyToManyField(question,null=True,related_name='dislike')
    liked=models.ManyToManyField(question,null=True,related_name='liked')
    visited=models.ManyToManyField(question,null=True,related_name='visited')







