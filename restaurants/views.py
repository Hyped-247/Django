from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView
from django.views.generic import CreateView
from .models import RestaurantsLocations
from .forms import RestaurantsLocationsCreateForm


class RestaurantListView(LoginRequiredMixin, ListView):
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        return RestaurantsLocations.objects.filter(owner=self.request.user)


class RestaurantDetailView(LoginRequiredMixin, DetailView):

    def get_queryset(self):
        return RestaurantsLocations.objects.filter(owner=self.request.user)

    # The way to make sure that you alone can access the data is make sure to add a decorator. That is,
    # what is going to force you to add a user name and password before accessing your information.


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantsLocationsCreateForm
    template_name = 'form.html'
    # success_url = '/restaurants/'
    # since we added LoginRequiredMixin we can use this: login_url =
    # if you allows want to be logged in, then you need change in in the settings file.
    login_url = '/login/'

    # This will allow you to accosiate each user with its data.
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantsLocationsCreateForm
    template_name = 'form.html'
    login_url = '/login/'

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context

    def get_queryset(self):
        return RestaurantsLocations.objects.filter(owner=self.request.user)
