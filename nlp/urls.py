from django.contrib import admin
from django.urls import path
from nlp import views

app_name = 'nlp'

urlpatterns = [
    path('sentiment/', views.sentiment, name='nlp_sentiment')
]
