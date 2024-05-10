from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Client, Domain
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

@login_required
def index(request):
    return HttpResponse("PUBLIC.")

from .models import Client, Domain

def create_user_and_tenant(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            tenant = Client(schema_name=user.username, name=user.username)
            tenant.save()
            tenant_domain = f"{user.username}.localhost" if request.META['HTTP_HOST'] == 'localhost:8000' else f"{user.username}.bootrix.com"
            
            domain = Domain(domain=tenant_domain, tenant=tenant, is_primary=True)
            domain.save()

            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'create_user.html', {'form': form})


def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                print(authenticate(username=username, password=password))
                tenant_domain = f"{user.username}.localhost:8000" if request.META['HTTP_HOST'] == 'localhost:8000' else f"{user.username}.bootrix.com"
                
                if user is not None:
                    login(request, user)
                    return redirect('http://' + tenant_domain)

        else:
            form = AuthenticationForm()
        
        return render(request, 'login.html', {'form': form})