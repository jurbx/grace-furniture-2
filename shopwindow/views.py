from django.shortcuts import render
from .models import MainImages, ImgUnderMainImage, ShopWindowLowerSlider, \
    ShopWindowUpperSlider, ShopWindowImages, ImgUnderLowerSlider


def shopwindow(request):
    main_img = MainImages.objects.all()
    img_under_main_image = ImgUnderMainImage.objects.all()
    upper_slider = ShopWindowUpperSlider.objects.all()
    lower_slider = ShopWindowLowerSlider.objects.all()
    images = ShopWindowImages.objects.all()
    second_images = ImgUnderLowerSlider.objects.all()
    if img_under_main_image:
        if len(img_under_main_image) > 6:
            img_under_main_image = img_under_main_image[:6]
    return render(request, 'shopwindow_en.html', context={'main_img': main_img,
                                                       'img_under_main_image': img_under_main_image,
                                                       'upper_slider': upper_slider,
                                                       'images': images,
                                                       'lower_slider': lower_slider,
                                                       'second_images': second_images
                                                       })
