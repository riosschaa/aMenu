from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Restaurant, RestaurantCategory
from .forms import RestaurantForm, RestaurantUpdateForm
from menu.models import Menu
import cloudinary


# Create your views here.

def restaurantslist(request):
    print(request)
    restaurants = Restaurant.objects.filter(private=False)
    restaurantcategories = RestaurantCategory.objects.all()
    for resto in restaurants:
        print(resto.logo)
    return render(request, "restaurants/restaurantsList.html", {'restaurants': restaurants,
                                                                'restaurantcategories': restaurantcategories})


@login_required
def myrestaurants(request):
    restaurants = Restaurant.objects.filter(user=request.user.id)
    menuList = Menu.objects.filter(restaurant__in=restaurants)
    menudict = {}
    for resto in restaurants:
        menu = []
        for menus in menuList:
            if menus.restaurant.id == resto.id:
                menu.append(menus)

        menudict[resto.name] = menu

    return render(request, "restaurants/restaurant_list.html", {'restaurants': restaurants,
                                                                'menuDict': menudict,
                                                                })


class RestaurantListView(ListView):
    model = Restaurant


class RestaurantCreate(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    success_url = reverse_lazy('myrestaurants')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)


class RestaurantUpdate(UpdateView):
    model = Restaurant
    form_class = RestaurantUpdateForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('myrestaurants')
