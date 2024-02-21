from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)



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
    upload = models.ImageField(upload_to=user_directory_path)
    content = models.TextField()
    author = models.CharField(max_length=120)
    author_post = models.ForeignKey(User, on_delete=models.CASCADE)
    index = models.CharField(max_length=1)
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
    author_post = models.ForeignKey(User, on_delete=models.CASCADE)
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
    author_post = models.ForeignKey(User, on_delete=models.CASCADE)
    solution = models.ForeignKey('Solution', on_delete=models.CASCADE)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-published_at']