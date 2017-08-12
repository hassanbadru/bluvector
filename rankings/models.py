# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Brewery Model
class Brewery(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name

# Beer model
class Beer(models.Model):
    name = models.CharField(max_length=255)
    brewery = models.ForeignKey(Brewery, related_name='beers')
    style = models.CharField(max_length=255)
    abv = models.DecimalField(max_digits=2, decimal_places=0, verbose_name="Alcohol by Volume (%)", blank=False)
    description = models.TextField()

    def __str__(self):
        return "{0}".format(self.name)


# Review Model
class Review(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=255)
    ranking = models.IntegerField()
    comment = models.TextField()
    beer = models.ForeignKey(Beer, related_name="reviews", null = True)

    def true_ranking(self):
        return self.ranking * 20

    def total_ranking(self):
        return sum([i for i in self.ranking])

    def __str__(self):
        return "{0} - {1} - {2}".format(self.username, self.beer, self.ranking)
