from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def details(request):
    return render(request, 'details.html')

def registry(request):
    return render(request, 'registry.html')

def rsvp(request):
    return render(request, 'rsvp.html')

def photos(request):
    return render(request, 'photos.html')

