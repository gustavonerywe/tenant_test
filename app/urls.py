from app.views import index
from django.urls import path
from django.contrib import admin

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', index),
]