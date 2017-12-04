from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from .models import RestaurantsLocations
from .forms import RestaurantsLocationsCreateForm


class RestaurantListView(ListView):
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantsLocations.objects.filter(
                Q(category__iexact=slug) | Q(category__contains=slug)
            )
        else:
            queryset = RestaurantsLocations.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantsLocations.objects.all()

# The way to make sure that you alone can access the data is make sure to add a decorator. That is,
# what is going to force you to add a user name and password before accessing your information.


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantsLocationsCreateForm
    template_name = 'restaurants/form.html'
    success_url = '/restaurants/'
    # since we added LoginRequiredMixin we can use this: login_url =
    # if you allows want to be logged in, then you need change in in the settings file.
    login_url = '/login/'

    # This will allow you to accosiate each user with its data.
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)


class PasswordReset(PasswordResetView):
    template_name = 'registration/password_reset_form.html'

