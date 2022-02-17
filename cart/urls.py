from django.urls import path
from .views import cart_view, model_view, CreateModelView, EditModelView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', cart_view, name='cart_view'),
    path('detail/<slug:slug>/', model_view, name='model_view'),
    path('create/', CreateModelView.as_view(), name='model_create'),
    path('edit/<slug:slug>/', login_required(EditModelView.as_view()), name='model_edit'),
]
