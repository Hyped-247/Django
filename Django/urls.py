"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView

from restaurants.views import RestaurantListView, RestaurantCreateView, RestaurantDetailView

urlpatterns = [
    # core
    url(r'^admin/', admin.site.urls),
    url(r'^base/$', TemplateView.as_view(template_name='base.html')),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^content/$', TemplateView.as_view(template_name='content.html')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),

    # restaurants
    url(r'^restaurants/$', RestaurantListView.as_view()),
    url(r'^restaurants/create/$', RestaurantCreateView.as_view()),
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),

]

