from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    # Path del core
    path('', views.restaurantslist, name="restaurants"),

=======
from django.contrib.auth.decorators import login_required
from . import views
from .views import RestaurantCreate, RestaurantUpdate, RestaurantListView

urlpatterns = [
    # Path del core
    path('all/', views.restaurantslist, name="restaurants"),
    path('owner/', views.myrestaurants, name="myrestaurants"),
    path('create/', login_required(views.RestaurantCreate.as_view()), name="createRestaurant"),
    path('update/<int:pk>/', login_required(views.RestaurantUpdate.as_view()), name="updateRestaurant"),
>>>>>>> version 1
]
