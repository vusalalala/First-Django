import os
print (os.getcwd())

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pages'),
   ]