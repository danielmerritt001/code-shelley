from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('codes/', views.code_index, name='code-index'),
  path('codes/<int:code_id>/', views.code_detail, name='code-detail'),
  path('codes/create/', views.CodeCreate.as_view(), name='code-create'),
  path('codes/<int:pk>/update/', views.CodeUpdate.as_view(), name='code-update'),
  path('codes/<int:pk>/delete/', views.CodeDelete.as_view(), name='code-delete'),
  path('accounts/signup/', views.signup, name='signup'),
]