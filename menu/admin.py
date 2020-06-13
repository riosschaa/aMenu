from django.contrib import admin
from .models import Menu, Restaurant, Preparations, PreparationCategory, PreparationType


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PreparationsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PreparationTypesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PreparationCategoriesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Menu, MenuAdmin)
admin.site.register(Preparations, PreparationsAdmin)
admin.site.register(PreparationCategory, PreparationCategoriesAdmin)
admin.site.register(PreparationType, PreparationTypesAdmin)
