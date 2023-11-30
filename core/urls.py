from django.urls import path
from . import views

#urls go here budd!!

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]