from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='posts'),
    path('post/create/', views.create_post, name='post-create'),
    path('post/edit/<int:id>/', views.edit_post, name='post-edit'),
    path('post/delete/<int:id>/', views.delete_post, name='post-delete'),
    path('task/create/', views.create_task, name='task-create'),
    path('task/edit/<int:id>/', views.edit_task, name='task-edit'),
    path('task/delete/<int:id>/', views.delete_task, name='task-delete'),
    path('course/create/', views.create_course, name='course-create'),
    path('course/edit/<int:id>/', views.edit_course, name='course-edit'),
    path('course/delete/<int:id>/', views.delete_course, name='course-delete'),
    path('solution/create/', views.create_solution, name='solution-create'),
    path('solution/edit/<int:id>/', views.edit_solution, name='solution-edit'),
    path('solution/delete/<int:id>/', views.delete_solution, name='solution-delete'),
    path('about/', views.about, name='about'),
    path('math/', views.math, name='math'),
    path('math-task/', views.math_task, name='math-task'),
    path('phisics/', views.phisics, name='phisics'),
    path('phisics-task/', views.phisics_task, name='phisics-task'),
    path('it/', views.it, name='it'),
    path('it-task/', views.it_task, name='it-task'),
    path('sandbox/', views.sandbox, name='sandbox'),
    path('task-list/', views.task_list, name='task-list'),
    path('task/', views.task, name='task')
]