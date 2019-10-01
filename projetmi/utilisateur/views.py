from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'pages/contact/contact.html')

def register(request):
    return render(request, 'pages/contact/register.html')