from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="client_index"),
    path('create/', views.create_object, name="client_create"),
    path('show/', views.showModels, name="client_show"),
    path('page/', views.page, name='page'),
]