from django.contrib import admin
from .models import HeroSection, ShopWindow, AboutUs


# class ThingInfoInline(admin.StackedInline):
#     model = ThingInfo
#     max_num = 3
#
#
# admin.site.register(MainMenu)
#
#
admin.site.register(HeroSection)
admin.site.register(ShopWindow)
admin.site.register(AboutUs)
#
#
# admin.site.register(Services)
#
#
# admin.site.register(DetailMenu)
#
#
# @admin.register(MainThing)
# class MainThingAdmin(admin.ModelAdmin):
#     list_display = ['title', 'desc', 'img']
#     inlines = [ThingInfoInline]
