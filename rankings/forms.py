from django import forms
from django.forms import ModelForm
from .models import Beer, Review

class ProductForm(ModelForm):
    class Meta:
        model = Beer
        fields = ['name', 'brewery', 'style', 'abv', 'description']

class ReviewForm(ModelForm):
    class Meta:

        model = Review
        fields = ['username', 'comment']

        widgets = {
          'comment': forms.Textarea(attrs={'rows':3, 'cols':20}),
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['comment'].required = False
