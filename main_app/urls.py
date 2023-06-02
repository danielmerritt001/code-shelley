from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('codes/', views.code_index, name='code-index'),
  path('codes/<int:code_id>/', views.code_detail, name='code-detail'),
]