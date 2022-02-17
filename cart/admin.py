from django.contrib import admin
from .models import SofaModels, Cart3dModels, CartImages, SofaModel, SofaColor, SofaTypes


class Cart3dModelsInline(admin.StackedInline):
    model = Cart3dModels
    max_num = 1


class CartImagesInLine(admin.StackedInline):
    model = CartImages
    extra = 1


@admin.register(SofaModel)
class CartSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc']
    readonly_fields = ['slug']
    inlines = [CartImagesInLine, Cart3dModelsInline]


admin.site.register(SofaModels)
admin.site.register(SofaColor)
admin.site.register(SofaTypes)