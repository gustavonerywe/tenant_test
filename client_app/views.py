from django.shortcuts import render
from django.http import HttpResponse
from .forms import TestModelForm
from .models import TestModel

def index(request):
    return render(request, 'create_object.html')

def create_object(request, name):
    model = TestModel(name=name)
    model.save()
    return HttpResponse(f"Object created. {model.name}")
