from test import test
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'photos' : test()}
    return render(request, 'html/index.html', context)