import datetime

import boto
from django.conf import settings
from django.shortcuts import render

def index(request):

    context = {'base_url': settings.STATIC_URL}
    return render(request, 'poll/index.html', context)