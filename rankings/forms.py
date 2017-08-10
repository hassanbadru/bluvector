from django.forms import ModelForm
from .models import Beer, Review

class ProductForm(ModelForm):
    class Meta:
        model = Beer
        fields = ['name', 'brewery', 'style', 'abv', 'description']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['username', 'ranking', 'comment', 'beer']
