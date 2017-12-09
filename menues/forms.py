from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'contents',
            'name',
            'restaurant',
            'excludes',
            'public',
        ]

    def __init__(self, user=None,  *args, **kwargs):
        # print(kwargs.pop('user'))
        print(user)
        super(ItemForm, self).__init__(*args, **kwargs)


