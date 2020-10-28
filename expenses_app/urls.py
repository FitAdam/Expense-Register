"""Defines URL patterns for expenses_app."""

from django.urls import path

from . import views

app_name = 'expenses_app'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('new_expense/', views.new_expense, name='new_expense'),
    path('analysis/', views.analysis, name='analysis'),
   
]