from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.scan_code, name='scan_code'),
    path('admit/', views.admit_code, name='admit_code'),
]
