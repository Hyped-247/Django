from django import forms
from .models import Item
from .models import RestaurantsLocations


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

    def __init__(self, user=None, *args, **kwargs):
        # print(kwargs.pop('user'))
        print(user)
        print(kwargs)
        super(ItemForm, self).__init__(*args, **kwargs)
        # .exclude(item__isnull=False)
        self.fields['restaurant'].queryset = RestaurantsLocations.objects.filter(owner=user)
