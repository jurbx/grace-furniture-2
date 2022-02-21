from django.contrib import admin
from .models import ImgUnderMainImage, ShopWindowImages, ShopWindowLowerSlider, MainImages, ShopWindowUpperSlider


admin.site.register(MainImages)
admin.site.register(ImgUnderMainImage)
admin.site.register(ShopWindowUpperSlider)
admin.site.register(ShopWindowLowerSlider)
admin.site.register(ShopWindowImages)

