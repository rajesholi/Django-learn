from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    return render(request, 'websites/index.html')  # Replace 'home.html' with your actual template
