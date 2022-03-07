from django.shortcuts import render
from app1.models import visit

from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.


def dashboard(request):
    
    return render(request, 'dash/dashboard.html')

def cmr(request):
    
    return render(request, 'dash/cmr.html')



