from django import forms


class AddProductInListForm(forms.Form):
    product_to_adding = forms.CharField(help_text="Введите название продукта")