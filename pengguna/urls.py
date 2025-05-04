from django.urls import path
from pengguna import views

urlpatterns = [
    path('', views.pengguna, name='pengguna'),
]