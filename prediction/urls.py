from django.urls import path
from . import views

app_name = 'prediction'

urlpatterns = [
    path('main/', views.main_view, name='main'),
]