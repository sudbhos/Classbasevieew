from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from .models import Company
# Create your views here.

class CompanyListView(ListView):
    model = Company

class CompanyDetailView(DetailView):
    model = Company

class CompanyCreateView(CreateView):
    model = Company
    fields = ["name","ceo","city","ctype"]

class CampanyUpdateView(UpdateView):
    model = Company
    fields = ["name","ceo","city","ctype"]
