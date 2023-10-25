# pylint: disable=all
# flake8: noqa

from django.shortcuts import render
from dash_app.models import Vgsales

def dashboard(request):
    db = Vgsales.objects.all()
    context = {'dados': db}
    return render(request, 'dash_app/pages/dashboard.html', context)
