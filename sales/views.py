from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.utils import timezone

from .models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = "sales/list.html"
    context_object_name = "customers"


class CustomerListSearchView(CustomerListView):
    def get_queryset(self):
        name = self.kwargs.get("name")
        queryset = super().get_queryset()
        if name:
            return queryset.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        return queryset


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "sales/detail.html"
    context_object_name = "customer"

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        return obj


def index(request):
    return HttpResponse("Hello, world. You're at the sales index.")
