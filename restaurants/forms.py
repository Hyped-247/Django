from django import forms
from .models import RestaurantsLocations


# This is how you can add things to the data base.
class RestaurantsLocationsCreateForm(forms.ModelForm):
    class Meta:
        model = RestaurantsLocations
        fields = [
            'name',
            'location',
            'category',
        ]

    def clean_location(self):
        location = self.cleaned_data.get('location')
        if location == 'Jeddah':
            raise forms.ValidationError('This cannot be the city since it is really cool')
        return location
