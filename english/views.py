from django.core.paginator import Paginator
from django.shortcuts import render

from cart.views import get_random3
from shopwindow.models import MainImages, ImgUnderMainImage, ShopWindowUpperSlider, ShopWindowLowerSlider, \
    ShopWindowImages, ImgUnderLowerSlider
from .models import HeroSectionEn, AboutUsEn
from main_page.models import ShopWindow
from contact.models import Contact, OurShops, TitleOurShop
from cart.models import SofaModels, SofaModel, SofaTypes, PaginatorLimit, CartImages, Cart3dModels


def index_english(request):
    hero = HeroSectionEn.objects.all().order_by('-priority')
    sofa_models = SofaModels.objects.filter(show_in_main_page=True)
    shopwindow = ShopWindow.objects.all()

    if contact := Contact.objects.all():
        contact = contact[0]

    if about := AboutUsEn.objects.all():
        about = about[0]

    return render(request, 'main_page_en.html', context={
        'shopwindow': shopwindow,
        'sofa_models': sofa_models,
        'hero': hero,
        'contact': contact,
        'about': about
    })


def cart_view_english(request):
    sofas = SofaModel.objects.all().order_by('-priority')
    if cur_category := request.GET.getlist('category'):
        sofas = sofas.filter(category__name__in=cur_category)
    if cur_type := request.GET.getlist('type'):
        sofas = sofas.filter(sofa_type__name_english__in=cur_type)

    max_page = 9
    paginator_limit = PaginatorLimit.objects.all()
    if paginator_limit:
        max_page = paginator_limit[0].number
    paginator = Paginator(sofas, max_page)
    page = request.GET.get('page')
    sofas = paginator.get_page(page)

    categories = SofaModels.objects.all()
    types = SofaTypes.objects.all()
    return render(request, 'cart_detail_2_en.html', context={'sofas': sofas,
                                                             'categories': categories,
                                                             'cur_category': cur_category,
                                                             'cur_type': cur_type,
                                                             'types': types})


def model_view_english(request, slug):
    sofa = SofaModel.objects.get(slug=slug)
    img = CartImages.objects.filter(sofa=sofa)
    more_sofa = get_random3(SofaModel, slug)
    if fbx := Cart3dModels.objects.filter(sofa__slug=slug):
        for item in fbx:
            fbx = item
    else:
        fbx = None
    return render(request, 'shop_product_detail_en.html', context={'sofa': sofa,
                                                                    'img': img,
                                                                    'more_sofa': more_sofa,
                                                                    'fbx': fbx})


def contact_view_english(request):
    if contact := Contact.objects.all():
        contact = contact[0]

    shop = OurShops.objects.all()
    if title := TitleOurShop.objects.all():
        title = title[0]
    return render(request, 'contact_en.html', context={'contact': contact, 'shop': shop, 'title': title})


def shopwindow_english(request):
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
