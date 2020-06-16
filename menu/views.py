from django.shortcuts import render, get_object_or_404
from .models import Menu, Restaurant, Preparations, PreparationCategory, PreparationType

# Create your views here.


def menu(request,resto_id):

    menus = Menu.objects.only('id').get(restaurant=resto_id).id
    preparations = Preparations.objects.filter(menu=menus)
    print (str(preparations))
    categories = PreparationCategory.objects.all()
    types = PreparationType.objects.all()
    #categories = ['Todo', 'Vegetariano']



    return render(request, "menu/menu.html", {'categories': categories,
                                              'preparations': preparations,
                                              'types': types})

