from django.urls import path
from .views import shopwindow


urlpatterns = [
    path('', shopwindow, name='shopwindow')
]