from django.urls import path
from . import views 

app_name = "weekend"

urlpatterns = [
    path('', views.index, name = 'index')
]