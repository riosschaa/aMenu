from django.shortcuts import render, get_object_or_404
from .models import Menu, Restaurant, Preparations, PreparationCategory, PreparationType

# Create your views here.


def menu(request):

    menus = Menu.objects.all()
    categories = PreparationCategory.objects.all()
    preparations = Preparations.objects.all()
    types = PreparationType.objects.all()
    #categories = ['Todo', 'Vegetariano']



    return render(request, "menu/menu.html", {'categories': categories,
                                              'menus': menus,
                                              'preparations': preparations,
                                              'types': types})

