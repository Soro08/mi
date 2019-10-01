from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'pages/index.html')

def detail(request):
    return render(request, 'pages/detail.html')

def fichier(request):
    return render(request, 'pages/fichier.html')

def profile(request):
    return render(request, 'pages/profile.html')