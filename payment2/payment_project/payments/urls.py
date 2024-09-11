from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment_form, name='payment_form'),
    path('charge/', views.charge, name='charge'),
]
