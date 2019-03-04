# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
def ship_list(request) :
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    workpath = os.path.dirname(os.path.abspath(__file__))
    column_names = ['IMO','Timestamp','Latitude','Longitude']
    c = open(os.path.join(workpath, 'positions.csv'), 'rb')
    df = pd.read_csv(c, names=column_names)
    position_list = df.order_by('-Timestamp')
    context_dict = {'positions': position_list}

    # Render the response and send it back!
    return render_to_response('ships/imo.html', context_dict, context)
