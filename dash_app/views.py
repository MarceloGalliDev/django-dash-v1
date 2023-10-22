from .dash_scripts import dash_app1
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dash_app/pages/dashboard.html')
