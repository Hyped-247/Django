from django.contrib.auth import get_user_model
from django.http import Http404
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from restaurants.models import RestaurantsLocations

User = get_user_model()


class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'

    def get_object(self, queryset=None):
        username = self.kwargs.get("username")
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        qs = RestaurantsLocations.objects.filter(owner=self.get_object())
        if qs.exists():
            context['locations'] = qs
        return context
