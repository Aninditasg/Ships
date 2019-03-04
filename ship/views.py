# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views import generic
from django.template import Context
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
import os
import pandas as pd

# Create your views here.
class ShipView(generic.ListView):
 def get_queryset (request):   
  workpath = os.path.dirname(os.path.abspath(__file__))
  column_names = ['IMO','Shipname']
  c = open(os.path.join(workpath, 'shipname.csv'), 'rb')
  df = pd.read_csv(c, names=column_names)
  b = df.to_html()
  context ={'loaded_data': b }  
  return render(request,"base.html",context)
