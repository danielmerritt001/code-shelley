from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('codes/', views.code_index, name='code-index')
]