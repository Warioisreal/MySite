from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser

def user_directory_path(instance, filename):
    return '{0}/{1}/{2}/user_{3}/{4}'.format(instance.index, instance.clas, instance.chapter_title, instance.user.id, filename)



class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    index = models.CharField(max_length=1)
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-published_at']

class Task(models.Model):
    title = models.CharField(max_length=120)
    chapter_title = models.CharField(max_length=120)
    upload = models.FileField(upload_to=user_directory_path)
    content = models.TextField()
    author = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    index = models.CharField(max_length=1)
    clas = models.CharField(max_length=2)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-published_at']

class Solution(models.Model):
    title = models.CharField(max_length=120)
    upload = models.ImageField(upload_to=user_directory_path)
    content = models.TextField()
    author = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate_count = models.IntegerField()
    rate_sum = models.IntegerField()
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-published_at']

class Comment(models.Model):
    title = models.CharField(max_length=120)
    upload = models.ImageField(upload_to=user_directory_path)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    solution = models.ForeignKey('Solution', on_delete=models.CASCADE)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-published_at']

class Course(models.Model):
    title = models.CharField(max_length=120)
    upload = models.ImageField(upload_to=user_directory_path)
    content = models.TextField()
    author = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    index = models.CharField(max_length=1)
    rate_count = models.IntegerField()
    rate_sum = models.IntegerField()
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-published_at']