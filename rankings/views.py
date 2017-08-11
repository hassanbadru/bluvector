# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse


from .models import Beer, Brewery, Review
from .forms import ReviewForm, ProductForm

import math
from datetime import *


class ReviewView(TemplateView):
    template_name = 'review.html'

    def get_context_data(self, **kwargs):
       context = super(ReviewView, self).get_context_data(**kwargs)
       context['all_beers'] = Beer.objects.all()
       context['breweries'] = Brewery.objects.all()

       # Pagination for All Beers
       num_beers = len(Beer.objects.all())
       p = int(math.ceil(float(num_beers)/8))
       context['beer_pages'] = [i for i in range(1, p+1)]

       num_of_reviews = []
       t_ranking = []
       last_review_date = []

       # Iterate through all beers
       for beer in context['all_beers']:

           # Query the reviews for each beer
           beer_reviews = Review.objects.filter(beer=beer)

           # Total number of reviews
           n_reviews = len(beer_reviews)

           #date of each review
           years = [i.date for i in beer_reviews]

           # Sort reviews by date
           if len(years) > 0:
               last_review_date.append(years[::-1])
           else:
                last_review_date.append(0)

           num_of_reviews.append(n_reviews)

           # Find ranking average of all ratings
           if n_reviews > 0:
               print([x.ranking for x in beer_reviews])
               avg_rating = (sum([x.ranking for x in beer_reviews]) / float(n_reviews)) * 20
           else:
               avg_rating = 0
           t_ranking.append(avg_rating)

       # Zip all instances needed by html template
       riterator = zip(num_of_reviews, context['all_beers'], t_ranking, last_review_date)

       # Sort all beers by average ranking
       context['by_rating'] = sorted(riterator, reverse=True, key = lambda t: t[2])

       # Sort all beers by date
       context['by_date'] = sorted(riterator, reverse=True, key = lambda t: t[3])

       # Add form from model
       context['forms'] = ProductForm()

       return context


    def post(self, request, *args, **kwargs):
        product_form = ProductForm(request.POST or None)
        if product_form.is_valid():
            save_form = product_form.save(commit = False)
            save_form.save()
            print(save_form.id)
            new_beer_id = int(save_form.id)

        # Redirects to the view product of product details and for review
        return HttpResponseRedirect(reverse('view-product', kwargs={'beer_id': new_beer_id}))



#View of Product and all feedback
class ProductView(TemplateView):

    template_name = 'product.html'
    context_object_name = "reviews"
    paginate_by = 4


    def get_context_data(self, beer_id):
       context = super(ProductView, self).get_context_data()

       # Catch 404
       try:
           context['beer_details'] = Beer.objects.get(pk=beer_id)
       except Beer.DoesNotExist:
           raise Http404("Such Beer Does Not Exist")

       # Gets instance of beer
       beer = context['beer_details']

       # Gets review model objects for an instance of beer
       context['reviews'] = sorted(Review.objects.filter(beer=beer), reverse= True)

       # Ranking of all reviews for beer
       t_ranks = [i.ranking for i in context['reviews']]

       # Calculates number of reviews
       context['num_of_reviews'] = len(t_ranks)

       # Calculates average of ranking
       if len(t_ranks) > 0:
           context['t_ranking'] = sum(t_ranks)/float(len(t_ranks)) * 20
       else:
           context['t_ranking'] = 0

       # Gets form from model
       context['forms'] = ReviewForm()

       # Includes pagination for reviews section
       paginator= Paginator(context['reviews'], self.paginate_by) # Shows 4 reviews per page

       # Creates reviews section as sets of 4
       page = self.request.GET.get('page')
       try:
           items = paginator.page(page)
       except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           items = paginator.page(1)

       except EmptyPage:
           # If page is out of range (e.g. 9999), deliver last page of results.
           items = paginator.page(paginator.num_pages)

       context['items'] = items

       return context


    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # Gets information about beer
        beer = context['beer_details']

        # Gets value of ranking submitteded
        rating = request.POST.get("ranking")

        feedback_form = ReviewForm(request.POST or None)

        if feedback_form.is_valid():
            save_form = feedback_form.save(commit = False)
            save_form.beer = beer #Adds beer instance
            save_form.ranking = int(rating) # Adds ranking submitted
            save_form.save()

            return HttpResponseRedirect('.')
