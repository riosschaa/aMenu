from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
import menu.views
import core.views
import restaurants.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", core.views.home, name="home"),
    path("restaurants/", restaurants.views.restaurantslist, name="restaurants"),
    path("menu/<int:resto_id>/", menu.views.menu, name="menu"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
