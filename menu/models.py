from django.db import models
from restaurants.models import Restaurant
from django.contrib.auth.models import User


# Create your models here.

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, verbose_name="Restaurant", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    activated = models.BooleanField(verbose_name="Activado", default=True)

    class Meta:

        unique_together = ('name', 'restaurant')
        verbose_name = "menu"
        verbose_name_plural = "menus"
        ordering = ['-created']

    def __str__(self):
        return self.name


class PreparationType(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tipo")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")


    class Meta:

    restaurant = models.ForeignKey(Restaurant, verbose_name="Restaurant", on_delete=models.CASCADE)
    used = models.BooleanField(verbose_name="En uso", default=False)

    class Meta:
        unique_together = ('name', 'restaurant')
        verbose_name = "tipo"
        verbose_name_plural = "tipos"
        ordering = ['-created']

    def __str__(self):
        return self.name

def custom_category_upload_to(instance, filename):
    old_instance = PreparationCategory.objects.get(pk=instance.pk)
    old_instance.image.delete()
    return 'category/' + filename



class PreparationCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre Categoria")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")


    # user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)

    class Meta:

    restaurant = models.ForeignKey(Restaurant, verbose_name="Restaurant", on_delete=models.CASCADE)
    used = models.BooleanField(verbose_name="En uso", default=False)
    image = models.ImageField(verbose_name="Imagen", upload_to="category", null=True, blank=True)

    class Meta:
        unique_together = ('name', 'restaurant')
        verbose_name = "Categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name

def custom_preparation_upload_to(instance, filename):
    old_instance = Preparations.objects.get(pk=instance.pk)
    old_instance.image.delete()
    return 'preparation/' + filename


class Preparations(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo", null=True, blank=True)
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to=custom_preparation_upload_to, null=True, blank=True)
    price = models.IntegerField(verbose_name="Precio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    menu = models.ManyToManyField(Menu, verbose_name="Menu", related_name="get_menu")
    type = models.ManyToManyField(PreparationType, verbose_name="Tipo", related_name="get_type")
    category = models.ManyToManyField(PreparationCategory, verbose_name="Categoria", related_name="get_category", blank=True)
    show_price = models.BooleanField(verbose_name="Muestra precio", default=True)
    activated = models.BooleanField(verbose_name="Activado", default=True)
    type = models.ManyToManyField(PreparationType, verbose_name="Tipo", related_name="get_type",
                                      blank=True)
    category = models.ManyToManyField(PreparationCategory, verbose_name="Categoria", related_name="get_category")
    show_price = models.BooleanField(verbose_name="Muestra precio", default=True)
    activated = models.BooleanField(verbose_name="Activado", default=True)

    class Meta:
        verbose_name = "plato"
        verbose_name_plural = "platos"
        ordering = ['-created']

    def __str__(self):
        return self.name
