from django.shortcuts import render
from django.shortcuts import redirect


def base(request):
    return redirect('home')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
