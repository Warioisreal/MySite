from django.contrib import admin
from .models import Post, Task, Solution, Comment


admin.site.register(Post)
admin.site.register(Task)
admin.site.register(Solution)
admin.site.register(Comment)