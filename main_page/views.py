from django.shortcuts import render
from .models import ShopWindow, HeroSection, AboutUs
from cart.models import SofaModels
from contact.models import Contact


def main_view(request):
    hero = HeroSection.objects.all().order_by('id')
    sofa_models = SofaModels.objects.all()
    shopwindow = ShopWindow.objects.all()

    if contact := Contact.objects.all():
        contact = contact[0]

    if about := AboutUs.objects.all():
        about = about[0]

    return render(request, 'main_page.html', context={
                                                      'shopwindow': shopwindow,
                                                      'sofa_models': sofa_models,
                                                      'hero': hero,
                                                      'contact': contact,
                                                      'about': about
                                                      })
