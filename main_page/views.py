from django.http import FileResponse
from django.shortcuts import render
from .models import ShopWindow, HeroSection, AboutUs
from cart.models import SofaModels
from contact.models import Contact



def main_view(request):
    hero = HeroSection.objects.all().order_by('-priority')
    sofa_models = SofaModels.objects.filter(show_in_main_page=True)
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


def test(request):
    import requests
    url = 'http://grace-furniture.com.ua//static/3C6437EAED8F3A81DEA63FB3EB1D40FB.txt'
    file = requests.get(url)
    return FileResponse(file)
