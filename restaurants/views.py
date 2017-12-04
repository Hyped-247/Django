from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from .models import RestaurantsLocations
from .forms import RestaurantsLocationsCreateForm

"""
def restaurant_createView(request):
    form = RestaurantsLocationsCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/restaurants/')
    if form.errors:
        print(form.errors)
    template_name = 'restaurants/form.html'
    context = {'form': form}
    return render(request, template_name, context)
"""


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


class RestaurantCreateView(CreateView):
    form_class = RestaurantsLocationsCreateForm
    template_name = 'restaurants/form.html'
    success_url = '/restaurants/'
    # This will allow you to accosiate each user with its data.

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)




