from django.urls import path
from . import views

urlpatterns = [
    # Path del core
    path('', views.menu, name="menu"),

]
