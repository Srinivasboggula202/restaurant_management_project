from django.urls import path
from .views import *

urlpatterns = [
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact_us),
    path('reservations/',views.reservations)
]