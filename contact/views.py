from django.shortcuts import render
from .models import Contact, OurShops


def contact_view(request):
    if contact := Contact.objects.all():
        contact = contact[0]

    shop = OurShops.objects.all()
    return render(request, 'contact.html', context={'contact': contact, 'shop': shop})
