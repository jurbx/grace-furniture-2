from django.shortcuts import render
from .models import Contact, OurShops, TitleOurShop


def contact_view(request):
    if contact := Contact.objects.all():
        contact = contact[0]

    shop = OurShops.objects.all()
    if title := TitleOurShop.objects.all():
        title = title[0]
    return render(request, 'contact.html', context={'contact': contact, 'shop': shop, 'title': title})
