# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Brewery(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name


class Beer(models.Model):
    name = models.CharField(max_length=255)
    brewery = models.ForeignKey(Brewery, related_name='beers')
    style = models.CharField(max_length=255)
    abv = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Alcohol by Volume")
    description = models.TextField()

    def __str__(self):
        return "{0} - {1}".format(self.name, self.brewery.name)


class Review(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    # For this exercise we don't need to register users,
    # let them input their username manually.
    username = models.CharField(max_length=255)
    ranking = models.IntegerField()
    review = models.TextField()
