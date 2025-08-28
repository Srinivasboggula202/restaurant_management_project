from django.urls import path
from .views import *

urlpatterns = [
    path('home/',views.home),
    path('about/',views.about),
    path('contact/',views.contact_us),
]