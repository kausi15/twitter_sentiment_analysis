from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tweets/', include('sentiment_analysis.urls')),
]