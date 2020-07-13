from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    # Path del core
    path('all/', views.restaurantslist, name="restaurants"),
    path('owner/', views.myrestaurants, name="myrestaurants"),
    path('create/', login_required(views.RestaurantCreate.as_view()), name="createRestaurant"),
    path('update/<int:pk>/', login_required(views.RestaurantUpdate.as_view()), name="updateRestaurant"),
]
