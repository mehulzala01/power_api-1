from django.contrib import admin
from django.urls import path
from vadc_dtau import views

app_name = 'vadc_dtau'

urlpatterns = [
    path('api_auth_token/', views.CustomAuthToken.as_view(), name='get_api_token'), 
    path('vadc_dtau/', views.vadc_dtau_cal, name='vadc_dtau_cal')
]
