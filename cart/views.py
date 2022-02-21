from django.core.paginator import Paginator
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify

from .models import SofaModel, CartImages, SofaModels, SofaTypes, Cart3dModels
import random
from django.views import generic


def get_random3(DBmodel, slug):
    model = DBmodel.objects.exclude(slug=slug)
    max_id = model.aggregate(max_id=Max("id"))['max_id']
    queryset = DBmodel.objects.none()
    while len(model) >= 6:
        pk = random.randint(1, max_id)
        category = DBmodel.objects.filter(pk=pk).first()
        if category:
            queryset |= DBmodel.objects.filter(pk=category.pk)
        if len(queryset) >= 6:
            return queryset
    return model


def three_d_model(request, slug):
    model = Cart3dModels.objects.get(sofa__slug=slug)
    return render(request, '3d_model.html', context={'file': model, 'slug': slug})


def cart_view(request):
    sofas = SofaModel.objects.all().order_by('-priority')
    if cur_category := request.GET.getlist('category'):
        sofas = sofas.filter(category__name__in=cur_category)
    if cur_type := request.GET.getlist('type'):
        sofas = sofas.filter(sofa_type__name__in=cur_type)

    paginator = Paginator(sofas, 9)
    page = request.GET.get('page')
    sofas = paginator.get_page(page)

    categories = SofaModels.objects.all()
    types = SofaTypes.objects.all()
    return render(request, 'cart_detail_2.html', context={'sofas': sofas,
                                                          'categories': categories,
                                                          'cur_category': cur_category,
                                                          'cur_type': cur_type,
                                                          'types': types})


def model_view(request, slug):
    sofa = SofaModel.objects.get(slug=slug)
    img = CartImages.objects.filter(sofa=sofa)
    more_sofa = get_random3(SofaModel, slug)
    if fbx := Cart3dModels.objects.filter(sofa__slug=slug):
        for item in fbx:
            fbx = item
    else:
        fbx = None
    return render(request, 'shop_product_detail.html', context={'sofa': sofa,
                                                                'img': img,
                                                                'more_sofa': more_sofa,
                                                                'fbx': fbx})
