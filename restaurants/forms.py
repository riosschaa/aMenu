from django import forms
from .models import Restaurant


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'url_logo', 'address', 'city', 'country', 'phone', 'email', 'type', 'category',
                  'private']
        boolean_choices = (
            (True, "Si"),
            (False, "No")
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Restaurant'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del restaurant'}),
            'logo': forms.FileInput(),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono de contacto'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'type': forms.CheckboxSelectMultiple(),
            'category': forms.CheckboxSelectMultiple(),
            'private': forms.RadioSelect(choices=boolean_choices)
        }
        labels = {
            "name": 'Nombre de Restaurant',
            "description": 'Descripción',
            "logo": 'Logo del plato',
        }


class RestaurantUpdateForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'logo', 'address', 'city', 'country', 'phone', 'email', 'type', 'category',
                  'private', 'activated']
        boolean_choices = (
            (True, "Si"),
            (False, "No")
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Restaurant'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del plato'}),
            'logo': forms.ClearableFileInput(),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono de contacto'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'type': forms.CheckboxSelectMultiple(),
            'category': forms.CheckboxSelectMultiple(),
            'private': forms.RadioSelect(choices=boolean_choices),
            'activated': forms.RadioSelect(choices=boolean_choices),
        }
        labels = {
            "name": 'Nombre de Restaurant',
        }
