from django.contrib import admin
from .models import Contact, OurShops, TitleOurShop


class OurShopsInline(admin.StackedInline):
    model = OurShops
    extra = 5


admin.site.register(Contact)


@admin.register(TitleOurShop)
class MainThingAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc']
    inlines = [OurShopsInline]