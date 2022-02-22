from contact.models import Contact
from .models import Logo, SocialNetwork


def menu(request):
    if contact := Contact.objects.all():
        contact = contact[0]

    if network := SocialNetwork.objects.all():
        network = network[0]

    if logo := SocialNetwork.objects.all():
        logo = logo[0]
    return {
        'contact': contact,
        'network': network,
        'logo': logo
    }