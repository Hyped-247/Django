from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView

from restaurants.views import (
    RestaurantListView,
    RestaurantCreateView,
    RestaurantDetailView,
)

urlpatterns = [
    # core
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^content/$', TemplateView.as_view(template_name='content.html'), name='content'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
]
















