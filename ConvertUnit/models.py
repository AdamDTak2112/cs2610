# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Convert(models.Model):
    factors = {'g': 1, 't_oz': 31.10348, 'lbs': 453.5924, 'kg': 1000, 'ton': 1000000, 'oz': 28.34952}
    def __str__(self):
        return self.factors