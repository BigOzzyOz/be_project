from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customer/", views.CustomerListView.as_view(), name="customer"),
    path("customer/<int:pk>", views.CustomerDetailView.as_view(), name="customer_detail"),
    path("customer/<str:name>", views.CustomerListSearchView.as_view(), name="customer_search"),
]
