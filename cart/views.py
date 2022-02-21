from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify

from .models import SofaModel, CartImages, SofaModels, SofaTypes, Cart3dModels
import random
from .forms import SofaCreateForm, SofaEditForm, ImageForm, FbxForm
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


class CreateModelView(generic.CreateView):
    model = SofaModel
    template_name = 'shop_product_create.html'
    success_url = reverse_lazy('cart_view')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_form'] = ImageForm()
        context['fbx_form'] = FbxForm()
        return context

    def form_valid(self, form):
        self.object = form.save()
        self.object.slug = slugify(self.object.title)
        self.object.save()

        fbx_form = FbxForm(self.request.POST, self.request.FILES, instance=self.object)
        if fbx_form.is_valid():
            fbx_form.save()

        image_form = ImageForm(self.request.POST, self.request.FILES, instance=self.object)
        if image_form.is_valid():
            image_form.save()
        return HttpResponseRedirect(self.get_success_url())


class EditModelView(generic.UpdateView):
    model = SofaModel
    template_name = 'shop_product_edit.html'
    success_url = reverse_lazy('model_view')
    form_class = SofaEditForm

    def get_success_url(self):
        return reverse('model_view', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            context['image_form'] = ImageForm(self.request.POST, self.request.FILES, instance=self.object)
            context['fbx_form'] = FbxForm(self.request.POST, self.request.FILES, instance=self.object)
        else:
            context['image_form'] = ImageForm(instance=self.object)
            context['fbx_form'] = FbxForm(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        image_form = context['image_form']
        fbx_form = context['fbx_form']

        self.object = form.save()
        self.object.slug = slugify(self.object.title)

        if fbx_form.is_valid():
            fbx_form.save()

        if image_form.is_valid():
            image_form.save()
        return super(EditModelView, self).form_valid(form)