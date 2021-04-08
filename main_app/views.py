from django.shortcuts import render
from django.shortcuts import render

#Home view:
def home(request):
    return render(request, 'home.html')
    # return render(request, 'home.html', {'recipes': recipes})

#About view:
def about(request):
    return render(request, 'about.html')

