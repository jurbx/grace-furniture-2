from contact.models import Contact


def footer(request):
    if contact := Contact.objects.all():
        contact = contact[0]
    return {'contact': contact}