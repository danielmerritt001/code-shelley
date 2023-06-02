from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Code


# CBVs
class CodeCreate(CreateView):
  model = Code 
  fields = '__all__'
  success_url = '/codes/'



# View Functions
def home(request):
  return render(request, 'home.html')

def code_index(request):
  codes = Code.objects.all()
  return render(request, 'codes/index.html', { 'codes' : codes})

def code_detail(request, code_id):
  code = Code.objects.get(id=code_id)
  return render(request, 'codes/detail.html', { 'code': code })