from django.contrib import admin
from .models import Restaurant, RestaurantCategory, RestaurantType


# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class RestaurantTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class RestaurantCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantType, RestaurantTypeAdmin)
admin.site.register(RestaurantCategory, RestaurantCategoryAdmin)
