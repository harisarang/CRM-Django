from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('product/', views.product, name="product")
]