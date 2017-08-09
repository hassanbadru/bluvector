# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.views.generic import DetailView

from django.shortcuts import render
from .models import Beer, Brewery

import math


'''

def index(request):
    all_beers = Beer.objects.all()
    return render(request, 'review.html', {'all_beers': all_beers})
'''
'''
class IndexView(TemplateView):
    template_name = 'review.html'

    def index(self):
        return {'all_beers': Beer.objects.all()}

class ReviewView(DetailView):

    context_object_name = "beer"
    queryset = Beer.objects.all()
'''

class ReviewView(TemplateView):
    template_name = 'review.html'
    def get_context_data(self, **kwargs):
       context = super(ReviewView, self).get_context_data(**kwargs)
       context['all_beers'] = Beer.objects.all()
       context['breweries'] = Brewery.objects.all()

       num_beers = len(Beer.objects.all())
       #p = num_beers / 8
       p = int(math.ceil(float(num_beers)/8))
       context['beer_pages'] = [i for i in range(1, p+1)]
       return context





class ProductView(TemplateView):
    template_name = 'product.html'
    def get_context_data(self, beer_id):
       context = super(ProductView, self).get_context_data()
       #context['all_beers'] = Beer.objects.all()
       context['pdetails'] = Beer.objects.get(pk=beer_id)
       return context
