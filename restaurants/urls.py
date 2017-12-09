from django.conf.urls import url


from .views import (
    RestaurantListView,
    RestaurantCreateView,
    RestaurantDetailView,
)


urlpatterns = [
    # restaurants
    url(r'create/$', RestaurantCreateView.as_view(), name='create'),
    url(r'(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
    url(r'$', RestaurantListView.as_view(), name='list'),
]

