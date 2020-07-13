from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class RestaurantType(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tipo")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    #user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "tipo"
        verbose_name_plural = "tipos"
        ordering = ['-created']

    def __str__(self):
        return self.name


class RestaurantCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre Categoria")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    # user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name

def custom_upload_to(instance, filename):
    old_instance = Restaurant.objects.get(pk=instance.pk)
    old_instance.logo.delete()
    return 'logo/' + filename


class Restaurant(models.Model):
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="Titulo")

    address = models.CharField(max_length=200, verbose_name="Dirección")
    phone = models.CharField(max_length=200, verbose_name="Teléfono")
    email = models.CharField(max_length=200, verbose_name="Email", null=True, blank=True)
    city = models.CharField(max_length=200, verbose_name="Ciudad")
    country = models.CharField(max_length=200, verbose_name="País")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    logo = models.ImageField(verbose_name="Logo", upload_to="services", null=True, blank=True)
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    address = models.CharField(max_length=200, verbose_name="Dirección")
    city = models.CharField(max_length=200, verbose_name="Ciudad")
    country = models.CharField(max_length=200, verbose_name="País")
    phone = models.CharField(max_length=200, verbose_name="Teléfono")
    email = models.CharField(max_length=200, verbose_name="Email", null=True, blank=True)
    logo = models.ImageField(verbose_name="Logo", upload_to=custom_upload_to, null=True, blank=True)
    private = models.BooleanField(verbose_name="Restaurant Privado", default=False)
    type = models.ManyToManyField(RestaurantType, verbose_name="Tipo", related_name="get_type")
    category = models.ManyToManyField(RestaurantCategory, verbose_name="Categoria", related_name="get_category")
    activated = models.BooleanField(verbose_name="Activado", default=True)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        unique_together = ('name', 'user', 'address', 'city', 'country')
        verbose_name = "restaurant"
        verbose_name_plural = "restaurants"
        ordering = ['-created']

    def __str__(self):
        return self.name
