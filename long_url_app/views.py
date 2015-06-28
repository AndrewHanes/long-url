# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from long_url_app import models


def forwarder(request, ident=None):
    url = models.Resolver.objects.filter(ident=ident)
    if len(url) > 0:
        return redirect(url[0].to)
    raise Exception("Cannot find ident")


def index(request):
    return redirect('static/index.html')
