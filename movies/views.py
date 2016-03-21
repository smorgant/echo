from django.shortcuts import render
from django.template import loader

from .models import Movie

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def manage(request):
    movies_list = Movie.objects.order_by('title')[:10]
    template = loader.get_template('movies/manage.html')
    context = {
        'movies_list': movies_list,
    }
    return HttpResponse(template.render(context, request))

def wanted(request):
    response = "You're looking at the results of Wanted"
    return HttpResponse(response)