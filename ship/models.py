# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Ship(models.Model):
    ship_imo= models.CharField(max_length=20)
    ship_name= models.CharField(max_length=200)
    
class Meta:
      verbose_name = ("Ship")
      verbose_name_plural = ("Ships")
