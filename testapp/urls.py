
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("",views.CompanyListView.as_view(),name="CompanyListView"),
    path('<int:pk>',views.CompanyDetailView.as_view(),name="CompanyDetailView"),
    path("CompanyCreateView",views.CompanyCreateView.as_view(),name="CompanyCreateView"),
    path('update/<int:pk>',views.CampanyUpdateView.as_view(),name="CampanyUpdateView"),
    path('delete/<int:pk>',views.CompanyDeleteViews.as_view(),name="CompanyDeleteViews"),

]
