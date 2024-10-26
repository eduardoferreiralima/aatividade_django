from django.urls import path
from .views import base
from . import views

urlpatterns = [
    path('', base, name='base'),
    path('criar_enquete/', views.criar_enquete, name='criar_enquete')
]
