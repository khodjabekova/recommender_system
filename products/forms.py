from django import forms
from .models import Product, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'text', 'image')


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('text', 'rate')

        widgets = {
            'text': forms.Textarea(attrs={'class': 'textinputclass'}),
        }
