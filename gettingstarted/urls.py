from django.urls import path, include
from django.conf import settings
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
<<<<<<< HEAD
    path("", core.views.home, name="home"),
    path("restaurants/", restaurants.views.restaurantslist, name="restaurants"),
    path("menu/<int:resto_id>/", menu.views.menu, name="menu"),
=======
    #path("", core.views.home, name="home"),
    #path("restaurants/", restaurants.views.restaurantslist, name="restaurants"),
    #path("menu/<int:resto_id>/", menu.views.menu, name="menu"),
        # Path core
    path('', include('core.urls')),

    # Path menu
    path('menu/', include('menu.urls')),

    # Path Restaurant List
    path('restaurants/', include('restaurants.urls')),

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

    
>>>>>>> version 1
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

