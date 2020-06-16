from django.urls import path
from . import views

urlpatterns = [
    # Path del core
    path('<int:resto_id>/', views.menu, name="menu"),

]
