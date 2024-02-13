from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='posts'),
    path('post/create/', views.create_post, name='post-create'),
    path('post/edit/<int:id>/', views.edit_post, name='post-edit'),
    path('post/delete/<int:id>/', views.delete_post, name='post-delete'),
    path('about/', views.about, name='about'),
    path('math/', views.math, name='math'),
    path('math-task/', views.math_task, name='math-task'),
    path('phisics/', views.phisics, name='phisics'),
    path('phisics-task/', views.phisics_task, name='phisics-task'),
    path('it/', views.it, name='it'),
    path('it-task/', views.it_task, name='it-task'),
    path('sandbox', views.sandbox, name='sandbox')
]