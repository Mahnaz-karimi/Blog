
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='repport-home'),
    path('about/', views.about, name='repport-about'),
]