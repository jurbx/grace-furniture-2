from django.shortcuts import render
from . import models
from cart.models import SofaModels


def main_view(request):
    hero = models.HeroSection.objects.all().order_by('id')
    sofa_models = SofaModels.objects.all()
    x = 0
    return render(request, 'main_page.html', context={
                                                      'sofa_models': sofa_models,
                                                      'hero': hero
                                                      })

