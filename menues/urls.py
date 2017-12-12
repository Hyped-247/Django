from django.conf.urls import url


from .views import (
    ItemListView,
    ItemDetailView,
    ItemUpdateView,
    ItemCreateView,
)
urlpatterns = [
    url(r'create/$', ItemCreateView.as_view(), name='create'),
    url(r'(?P<pk>[\w-]+)/$', ItemUpdateView.as_view(), name='detail'),
    url(r'$', ItemListView.as_view(), name='list'),
]
