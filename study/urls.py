from django.urls import path
from . import views

#urls go here budd!!

urlpatterns = [
    path('', views.home, name='study-home'),
    path('resources/', views.resources, name='study-resources'),
]