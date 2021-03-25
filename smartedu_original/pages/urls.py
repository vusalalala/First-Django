from pages.views import AboutView, IndexView, ContactView
from django.urls import path
import os
print(os.getcwd())


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
]
