from django.forms import ModelForm
from .models import Post, Task, Solution, Comment, Course
from django import forms

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
        'content',
        'author',
        'upload',
        'index',
        'clas',
        'chapter_title'
        ]
'''
{
'title': ['qwe'],
'content': ['qwe'],
'author': ['qwe'],
'upload': ['Scan_0290_FKoMIP0.jpg'],
'index': ['i'],
'clas': ['7'],
'chapter_title': ['Тема1']
}
'''
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
        'author',
        'index'
        ]