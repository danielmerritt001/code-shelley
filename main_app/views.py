from django.shortcuts import render
from .models import Code


# CBVs

# View Functions
def home(request):
  return render(request, 'home.html')

def code_index(request):
  codes = Code.objects.all()
  return render(request, 'codes/index.html', { 'codes' : codes})
