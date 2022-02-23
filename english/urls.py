from django.urls import path
from .views import index_english, cart_view_english, model_view_english, contact_view_english, shopwindow_english


urlpatterns = [
    path('', index_english, name='index_english'),
    path('catalog/', cart_view_english, name='cart_view_english'),
    path('catalog/detail/<slug:slug>/', model_view_english, name='model_view_english'),
    path('contact/', contact_view_english, name='contact_view_english'),
    path('shopwindow', shopwindow_english, name='shopwindow_english')
]