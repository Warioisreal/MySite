from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


"""def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)"""



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



"""class Task(model.Model):
    title = models.CharField(max_length=120)
    upload = models.FileField(upload_to=user_directory_path)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chapter = models.CharField(max_length=120)
    index = models.CharField(max_length=1)


    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-published_at']

class Solution(model.Model):"""
