
from django.contrib import admin
from django.urls import path
from scraperapp.views import home,home1

urlpatterns = [
    path('home/',home),
    path('bootcamp/',home1)
]

