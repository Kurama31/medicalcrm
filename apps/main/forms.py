from django import forms
from mptt.forms import TreeNodeChoiceField
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'parent']

    parent = TreeNodeChoiceField(queryset=MenuItem.objects.all())