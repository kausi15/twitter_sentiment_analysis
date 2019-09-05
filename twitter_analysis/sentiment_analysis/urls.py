from django.urls import path

from . import views

urlpatterns = [
    path('analysis', views.sentiment_analysis, name='analysis'),
]