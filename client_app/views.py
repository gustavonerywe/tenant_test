from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TestModelForm
from .models import TestModel
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html')

def create_object(request):
    form = TestModelForm()
    if request.method == 'POST':
        form = TestModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_show')
    else:
        form = TestModelForm()

    return render(request, 'create_object.html', {'form': form})

def showModels(request):
    models = TestModel.objects.all()
    return render(request, 'show_models.html', {'models': models})

def page(request):
    return render(request, 'page.html')