from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
groups = models.ManyToManyField(Group, related_name='auth_groups')

class User(AbstractUser):
    email=models.EmailField(null=False, max_length=150, unique=True)
    username=models.CharField(unique=True, max_length=100)


class Post(models.Model):
    title=models.CharField(max_length=225)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SocialMediaAccount(models.Model):
    accountName=models.CharField(max_length=150)
    platform = models.CharField(max_length=50)
    access_token = models.CharField(max_length=255)

    def __str__(self):
        return self.account_name


class Feed(models.Model): #its a collection of other ppls or yerasachn posts that is going to be displayed on the page
    name = models.CharField(max_length=255)
    description = models.TextField()
    accounts = models.ManyToManyField(SocialMediaAccount)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feeds_created')
    is_public = models.BooleanField()
    followers = models.ManyToManyField(User, related_name='feeds_following')
    posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_feeds')

    def __str__(self):
        return self.name
   

class Comment(models.Model):
    commentText=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}'s comment."