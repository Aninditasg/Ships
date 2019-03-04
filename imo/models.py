# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Position(models.Model):
     IMO = models.CharField(max_length=15)
     Timestamp = models.CharField(max_length=128)
     latitude = models.CharField(max_length=24)
     longitude = models.CharField(max_length=24)
   
     def __unicode__(self):
       return self.title