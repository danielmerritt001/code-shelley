from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Code


# CBVs
class Home(LoginView):
  template_name = 'home.html'

class CodeCreate(LoginRequiredMixin, CreateView):
  model = Code 
  fields = ['name', 'description', 'code', 'github', 'language', 'star']
  success_url = '/codes/'

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class CodeUpdate(LoginRequiredMixin, UpdateView):
  model = Code
  fields = ['description', 'code', 'github', 'language', 'star']

class CodeDelete(LoginRequiredMixin, DeleteView):
  model = Code
  success_url = '/codes/'

# View Functions

@login_required
def code_index(request):
  codes = Code.objects.filter(user=request.user)
  return render(request, 'codes/index.html', { 'codes' : codes})

@login_required
def code_detail(request, code_id):
  code = Code.objects.get(id=code_id)
  return render(request, 'codes/detail.html', { 'code': code })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('code-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)