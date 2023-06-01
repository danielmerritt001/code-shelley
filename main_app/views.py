from django.shortcuts import render
from django.http import HttpResponse


# CBVs

# View Functions
def home(request):
  return HttpResponse('<h1>Home Page</h1>')