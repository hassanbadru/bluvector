# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect
from .models import Beer, Brewery, Review

from .forms import ReviewForm, ProductForm

import math

from datetime import *

g_variables = {}

class ReviewView(TemplateView):
    template_name = 'review.html'
    def get_context_data(self, **kwargs):
       context = super(ReviewView, self).get_context_data(**kwargs)
       context['all_beers'] = Beer.objects.all()
       context['breweries'] = Brewery.objects.all()

       num_beers = len(Beer.objects.all())
       p = int(math.ceil(float(num_beers)/8))
       context['beer_pages'] = [i for i in range(1, p+1)]

       num_of_reviews = []
       t_ranking = []
       last_review_date = []

       for beer in context['all_beers']:
           beer_reviews = Review.objects.filter(beer=beer)
           n_reviews = len(beer_reviews)


           years = [i.date for i in beer_reviews]

           if len(years) > 0:
               last_review_date.append(years[::-1])
           else:
                last_review_date.append(0)


           #last_review_date.append([(i.date.year) for i in beer_reviews])

           num_of_reviews.append(n_reviews)

           if n_reviews > 0:
               avg_rating = (sum([x.ranking for x in beer_reviews]) / float(n_reviews)) * 20
           else:
               avg_rating = 0
           t_ranking.append(avg_rating)


       riterator = zip(num_of_reviews, context['all_beers'], t_ranking, last_review_date)
       context['by_rating'] = sorted(riterator, reverse=True, key = lambda t: t[2])
       context['by_date'] = sorted(riterator, reverse=True, key = lambda t: t[3])


       #self.request.POST
       context['forms'] = ProductForm(self.request.POST or None)
       return context





#View of Product and all feedback
class ProductView(TemplateView):
    template_name = 'product.html'
    def get_context_data(self, beer_id):
       context = super(ProductView, self).get_context_data()
       #context['all_beers'] = Beer.objects.all()
       context['beer_details'] = Beer.objects.get(pk=beer_id)
       beer = context['beer_details']

       context['reviews'] = Review.objects.filter(beer=beer)

       t_ranks = [i.ranking for i in context['reviews']]
       context['num_of_reviews'] = len(t_ranks)
       if len(t_ranks) > 0:
           context['t_ranking'] = sum(t_ranks)/float(len(t_ranks)) * 20
       else:
           context['t_ranking'] = 0

       context['forms'] = ReviewForm(self.request.POST or None)
       if context['forms'].is_valid():
           save_form = context['forms'].save(commit = False)
           save_form.save()
       return context
