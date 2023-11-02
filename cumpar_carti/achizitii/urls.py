from django.urls import path
from .views import *
 

app_name = "achizitii"
urlpatterns = [
    path('', view_index),
]
