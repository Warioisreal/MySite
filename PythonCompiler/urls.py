from django.urls import path
from . import views

urlpatterns = [
	path('compiler/', views.compiler, name='compiler'),
	path('compiler/runcode', views.runcode, name='runcode'),
]