from django import forms
from django.forms.models import inlineformset_factory
from .models import SofaModel, SofaModels, CartImages, Cart3dModels

GEEKS_CHOICES = (

)


class SofaCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'type': 'text'}))
    desc = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'type': 'text'}))
    main_image = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'id': 'image_input'}))
    category = forms.ModelChoiceField(queryset=SofaModels.objects.all())

    class Meta:
        model = SofaModel
        fields = ('title', 'desc', 'main_image', 'category')


class SofaEditForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'type': 'text', 'id': 'id'}))
    desc = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'type': 'text'}))
    main_image = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'id': 'image_input'}))
    category = forms.ModelChoiceField(queryset=SofaModels.objects.all())

    class Meta:
        model = SofaModel
        fields = ('title', 'desc', 'category', 'main_image')


ImageForm = inlineformset_factory(SofaModel, CartImages, max_num=6, extra=1, fields=('img', 'sofa'))
FbxForm = inlineformset_factory(SofaModel, Cart3dModels, max_num=1, fields=('fbx_file', 'sofa'))
