from django import forms
from .models import Menu, Preparations, PreparationType, PreparationCategory, Restaurant
from bootstrap_modal_forms.forms import BSModalModelForm


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu

        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del menu'}),
        }
        labels = {
            "name": '',
        }


class CreatePreparationForm(forms.ModelForm):
    class Meta:
        model = Preparations
        boolean_choices = (
            (True, "Si"),
            (False, "No")
        )

        fields = ['name', 'subtitle', 'description', 'price', 'image', 'type', 'category', 'show_price',
                  'activated']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del plato'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitulo del plato'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del plato'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'image': forms.FileInput(),
            'type': forms.CheckboxSelectMultiple(),
            'category': forms.CheckboxSelectMultiple(),
            'show_price': forms.RadioSelect(choices=boolean_choices),
            'activated': forms.RadioSelect(choices=boolean_choices),

        }
        labels = {
            "name": '',
            "subtitle": '',
            "description": '',
            "price": '',
            "image": 'Imagen del plato',
            "show_price": 'Mostrar precio',
            "activated": 'Activar',
        }

    def __init__(self, restoselect, *args, **kwargs):
        resto = restoselect
        super(CreatePreparationForm, self).__init__(*args, **kwargs)
        self.fields['type'].queryset = PreparationType.objects.filter(restaurant=resto)
        self.fields['category'].queryset = PreparationCategory.objects.filter(restaurant=resto)


## Prueba de bootstrap modal
class PreparationForm(BSModalModelForm):
    class Meta:
        model = Preparations
        fields = ['name', 'subtitle', 'description', 'price', 'image', 'type', 'category', 'show_price',
                  'activated']


class CategoryForm(BSModalModelForm):
    class Meta:
        model = PreparationCategory
        fields = ['name', 'image']


class TypeForm(BSModalModelForm):
    class Meta:
        model = PreparationType
        fields = ['name']
