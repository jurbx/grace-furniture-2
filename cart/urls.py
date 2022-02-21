from django.urls import path
from .views import cart_view, model_view, three_d_model
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', cart_view, name='cart_view'),
    path('detail/<slug:slug>/', model_view, name='model_view'),
    path('3d/detail/<slug:slug>/', three_d_model, name='three_d_model'),
]
