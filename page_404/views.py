from django.shortcuts import render
from .models import Page404


def handler404(request, *args, **kwargs):
    image = Page404.objects.all()
    response = render(request, '404_page.html', context={'img': image})
    response.status_code = 404
    return response


def handler500(request, *args, **kwargs):
    image = Page404.objects.all()
    response = render(request, '500_page.html', context={'img': image})
    response.status_code = 500
    return response