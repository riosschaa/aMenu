from django.shortcuts import render
from .models import Restaurant, RestaurantCategory


# Create your views here.

def restaurantslist(request):
    restaurants = Restaurant.objects.all()
    restaurantcategories = RestaurantCategory.objects.all()

    return render(request, "restaurants/restaurantsList.html", {'restaurants': restaurants,
                                                                'restaurantcategories': restaurantcategories})
