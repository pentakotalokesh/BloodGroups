from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('hereditary',views.webpage2,name='webpage2'),
    path('donate',views.webpage3,name='webpage3'),
    path('receive',views.webpage4,name='webpage4'),
    path('suggest',views.suggest,name='suggest'),
    path('donar_request',views.donar_request,name='donor_request'),
    path('recevier_request',views.recevier_request,name='recevier_request')
]