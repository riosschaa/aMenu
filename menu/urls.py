from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


urlpatterns = [
    # Path del core
    path('<int:resto_id>/<slug:restoname_slug>/', views.menu, name="menu"),
    path('menuadmin/<int:menu_id>/<int:resto_id>/', views.newmenu, name="menuadmin"),
    path('create/', login_required(views.MenuCreate.as_view()), name="createMenu"),

    #Model django bootstrap for preparations
    path('newMenuadmin/', views.Index.as_view(), name='newMenuAdmin'),
    path('createPreparation/', views.PrepCreateView.as_view(), name='create_preparation'),
    path('updatePreparation/<int:pk>/<int:menu_pk>/<int:resto_pk>', views.PreparationUpdateView.as_view(), name='update_preparation'),
    path('readPreparation/<int:pk>', views.PrepReadView.as_view(), name='read_preparation'),
    path('deletePreparation/<int:pk>/<int:menu_pk>/<int:resto_pk>', views.PrepDeleteView.as_view(), name='delete_preparation'),

    #Model django bootstrap for Category
    path('updatecategory/<int:pk>/<int:menu_pk>/<int:resto_pk>', views.CategoryUpdateView.as_view(), name='update_category'),
    path('deletecategory/<int:pk>/<int:menu_pk>/<int:resto_pk>', views.CategoryDeleteView.as_view(), name='delete_category'),

    # Model django bootstrap for Category
    path('updatetype/<int:pk>/<int:menu_pk>/<int:resto_pk>', views.TypeUpdateView.as_view(), name='update_type'),
    path('deletetype/<int:pk>/<int:menu_pk>/<int:resto_pk>', views.TypeDeleteView.as_view(), name='delete_type'),
]

