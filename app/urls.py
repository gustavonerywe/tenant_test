from app import views
from django.urls import path
from django.contrib import admin

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', views.index),
    path('accounts/login/', views.loginView, name='login'),
    path('create_user', views.create_user_and_tenant, name='create_user')
]