from django.forms import ModelForm
from .models import Post, Task, Solution, Comment, Course
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
        'title',
        'content',
        'index'
        ]

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
        'title',
        'chapter_title',
        'upload',
        'content',
        'author',
        'index'
        ]

class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = [
        'title',
        'upload',
        'content',
        'author'
        ]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
        'title',
        'upload',
        'content'
        ]

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = [
        'title',
        'upload',
        'content',
        'author'
        ]