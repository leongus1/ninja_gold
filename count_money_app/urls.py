from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('process_money/', views.count),
    path('reset/', views.reset),
    path('process_money/<str:location>/', views.count),
]