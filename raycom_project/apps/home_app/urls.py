# LOGIN ROUTE

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^account$', views.account),
    url(r'^store', views.store),
    url(r'^new_item', views.new_item),
    url(r'^show_item/(?P<id>\d+)$', views.show_item),
    url(r'^edit_profile/(?P<id>\d+)$', views.edit_profile),
    url(r'^checkout', views.checkout),
    url(r'^add_to_cart/(?P<id>\d+)$', views.add_to_cart),
]