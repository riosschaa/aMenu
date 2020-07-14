from django.urls import path, include
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

import hello.views
import menu.views
import core.views
import restaurants.views

urlpatterns = [

        # Path core
    path('', include('core.urls')),

    # Path menu
    path('menu/', include('menu.urls')),

    # Path Restaurant List
    path('restaurants/', include('restaurants.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),

    
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

