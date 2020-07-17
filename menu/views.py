from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Menu, Restaurant, Preparations, PreparationCategory, PreparationType
from .forms import MenuForm, CreatePreparationForm, PreparationForm, CategoryForm, TypeForm
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)


# Create your views here.


def menu(request, resto_id, restoname_slug):
    resto_id = resto_id
    #  if request.method == "POST":
    #      if 'restaurantselected' in request.POST:
    #          resto_id = request.POST.get('restaurantselected')

    menu_id = Menu.objects.only('id').get(restaurant=resto_id).id
    menu_name = Menu.objects.only('id').get(restaurant=resto_id).name
    preparations = Preparations.objects.filter(menu=menu_id)
    categorieswithpreparations = []
    for prep in preparations:
        for cat in prep.category.all():
            if cat.name not in categorieswithpreparations:
                categorieswithpreparations.append(cat.name)

    categories = PreparationCategory.objects.filter(restaurant=resto_id, name__in=categorieswithpreparations)
    types = PreparationType.objects.filter(restaurant=resto_id)

    return render(request, "menu/menu.html", {'categories': categories,
                                              'preparations': preparations,
                                              'types': types,
                                              'menuName': menu_name})


class MenuCreate(CreateView):
    model = Menu
    fields = ['restaurant', 'name']
    success_url = reverse_lazy('myrestaurants')

    def dispatch(self, request, *args, **kwargs):
        print(request.POST)
        return super(MenuCreate, self).dispatch(request, *args, **kwargs)


class CreateType(CreateView):
    model = PreparationType
    fields = ['name']


class CreateCategory(CreateView):
    model = PreparationType
    fields = ['name']


@login_required
def newmenu(request, menu_id, resto_id):
    resto = Restaurant.objects.get(id=resto_id)
    if request.user == resto.user:
        formprep = ''
        menuname = ''
        preparationslist = ''
        if menu_id is not 0:
            menuobj2 = Menu.objects.get(pk=menu_id)
            menuname = menuobj2.name
            resto = Restaurant.objects.get(id=menuobj2.restaurant.id)
            formprep = CreatePreparationForm(resto)
            preparationslist = Preparations.objects.filter(menu=menuobj2)

        typeslist = PreparationType.objects.filter(restaurant=resto)
        categorieslist = PreparationCategory.objects.filter(restaurant=resto)

        categoryname = ''
        typename = ''

        # print(resto.name)
        # print(request.POST)

        if request.method == "POST":
            if 'createmenu' in request.POST:
                # form = MenuForm(request.POST)
                menuname = request.POST.get('newmenuname')
                Menu.objects.create(name=menuname, restaurant=resto)

            elif 'editmenuname' in request.POST:
                menuname = request.POST.get('newmenuname')
                currmenuname = request.POST.get('editmenuname')
                menuobj = Menu.objects.get(name=currmenuname)
                menuobj.name = menuname
                menuobj.save()

            elif 'createnewcategory' in request.POST:
                categoryname = request.POST.get('newcategoryname')
                categoryimage = request.FILES.get('categoryimage')
                PreparationCategory.objects.create(name=categoryname, restaurant=resto, image=categoryimage)

            elif 'editcategoryname' in request.POST:
                categoryname = request.POST.get('editcategoryname')
                catnamecurr = request.POST.get('changenewcategory')
                catcurr = PreparationCategory.objects.get(name=catnamecurr)
                catcurr.name = categoryname
                catcurr.save()

            elif 'createnewtype' in request.POST:
                typename = request.POST.get('newtypename')
                PreparationType.objects.create(name=typename, restaurant=resto)

            elif 'edittypename' in request.POST:
                typename = request.POST.get('edittypename')
                typenamecurr = request.POST.get('changenewtype')
                typecurr = PreparationType.objects.get(name=typenamecurr)
                typecurr.name = typename
                typecurr.save()

            elif 'createnewpreparation' in request.POST:
                instance = Preparations.objects.create(name=request.POST.get('name'),
                                                       subtitle=request.POST.get('subtitle'),
                                                       description=request.POST.get('description'),
                                                       price=request.POST.get('price'),
                                                       image=request.FILES.get('image'),
                                                       show_price=request.POST.get('show_price'),
                                                       activated=request.POST.get('show_price'),
                                                       )
                instance.menu.add(menuobj2)
                print("categorias: ")
                for catid in request.POST.getlist('category'):
                    cat = PreparationCategory.objects.get(pk=catid)
                    print(cat)
                    instance.category.add(cat)
                print("Typo:")
                for typeid in request.POST.getlist('type'):
                    type = PreparationType.objects.get(pk=typeid)
                    print(type)
                    instance.type.add(type)

        return render(request, 'menu/newmenu.html', {'categoryname': categoryname,
                                                     'typename': typename,
                                                     'form2': formprep,
                                                     'typeslist': typeslist,
                                                     'categorieslist': categorieslist,
                                                     'menuname': menuname,
                                                     'preparationslist': preparationslist,
                                                     'menu_id': menu_id,
                                                     'resto_id': resto_id,

                                                     })
    else:
        print("DISTINTO USUARIO")
        return render(request, 'menu/error.html')


## implemente django-model-boostrap for preparations
class Index(ListView):
    model = Preparations
    context_object_name = 'preparations'
    template_name = 'menu/menuadmin.html'


# Create
class PrepCreateView(BSModalCreateView):
    template_name = 'preparation/create_preparation.html'
    form_class = PreparationForm
    success_message = 'Success: Preparation was created.'

    # success_url = reverse_lazy('menuadmin')
    def get_success_url(self):
        getid = str(self.request).split('/')
        menu_id = int(getid[4])
        resto_id = int(getid[5][:-2])
        return reverse_lazy('menuadmin', args=[menu_id, resto_id])


class PreparationCreateView(BSModalCreateView):
    template_name = 'preparation/create_preparation.html'
    form_class = PreparationForm
    success_url = reverse_lazy('menuadmin')


# Update
class PreparationUpdateView(BSModalUpdateView):
    model = Preparations
    template_name = 'preparation/update_preparation.html'
    form_class = PreparationForm

    # success_message = 'Success: Book was updated.'

    def get_success_url(self):
        getid = str(self.request).split('/')
        menu_id = int(getid[4])
        resto_id = int(getid[5][:-2])
        return reverse_lazy('menuadmin', args=[menu_id, resto_id])


# Read
class PrepReadView(BSModalReadView):
    model = Preparations
    template_name = 'preparation/read_preparation.html'


# Delete
class PrepDeleteView(BSModalDeleteView):
    model = Preparations
    template_name = 'preparation/delete_preparation.html'

    # success_message = 'Success: Book was deleted.'

    def get_success_url(self):
        getid = str(self.request).split('/')
        menu_id = int(getid[4])
        resto_id = int(getid[5][:-2])
        return reverse_lazy('menuadmin', args=[menu_id, resto_id])


## implemente django-model-boostrap for Cateogry
# Update
class CategoryUpdateView(BSModalUpdateView):
    model = PreparationCategory
    template_name = 'category/update_category.html'
    form_class = CategoryForm

    #  success_message = 'Success: Book was updated.'
    def get_success_url(self):
        getid = str(self.request).split('/')
        menu_id = int(getid[4])
        resto_id = int(getid[5][:-2])
        return reverse_lazy('menuadmin', args=[menu_id, resto_id])


# Delete
class CategoryDeleteView(BSModalDeleteView):
    model = PreparationCategory
    template_name = 'category/delete_category.html'

    # success_message = 'Success: Book was deleted.'

    def get_success_url(self):
        getid = str(self.request).split('/')
        menu_id = int(getid[4])
        resto_id = int(getid[5][:-2])
        return reverse_lazy('menuadmin', args=[menu_id, resto_id])


## implemente django-model-boostrap for Types
# Update

class TypeUpdateView(BSModalUpdateView):
    model = PreparationType
    template_name = 'type/update_type.html'
    form_class = TypeForm

    # success_message = 'Success: Book was updated.'

    def get_success_url(self):
        getid = str(self.request).split('/')
        menu_id = int(getid[4])
        resto_id = int(getid[5][:-2])
        return reverse_lazy('menuadmin', args=[menu_id, resto_id])


# Delete
class TypeDeleteView(BSModalDeleteView):
    model = PreparationType
    template_name = 'type/delete_type.html'
    success_message = 'Success: Book was deleted.'

    def get_success_url(self):
        getid = str(self.request).split('/')
        menu_id = int(getid[4])
        resto_id = int(getid[5][:-2])
        return reverse_lazy('menuadmin', args=[menu_id, resto_id])

