from django.shortcuts import render


# CBVs

# View Functions
def home(request):
  return render(request, 'home.html')