from django.urls import path
from .views import index, create_object

urlpatterns=[
    path('', index, name="client_index"),
]