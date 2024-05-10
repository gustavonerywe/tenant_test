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

from tenant_schemas.utils import schema_context
from .models import Client, Domain

def create_user_and_tenant(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Crie o usuário
            user = form.save()

            # Crie o tenant com o mesmo schema_name que o username
            tenant = Client.objects.create(schema_name=user.username, name=user.username)

            # Crie o schema
            tenant_domain = f"{user.username}.localhost:8000" if request.META['HTTP_HOST'] == 'localhost:8000' else f"{user.username}.bootrix.com"
            with schema_context(tenant.schema_name):
                # Associe o domínio ao schema
                domain = Domain.objects.create(
                    domain=tenant_domain,
                    tenant=tenant,
                    is_primary=True
                )

            # Redirecione para algum lugar após o sucesso
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
                tenant_domain = f"{user.username}.localhost:8000" if request.META['HTTP_HOST'] == 'localhost:8000' else f"{user.username}.bootrix.com"
                print(user)
                
                if user is not None:
                    login(request, user)
                    return redirect('http://' + tenant_domain)

        else:
            form = AuthenticationForm()
        
        return render(request, 'login.html', {'form': form})