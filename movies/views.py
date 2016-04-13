from django.shortcuts import render
from django.http import HttpResponse

import requests

from .models import Movie

# Views here:
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add(request, movie_imdbid):
    
    r = requests.get('http://www.omdbapi.com/', params = {'i':movie_imdbid,'plot':'short','r':'json'})
    
    
    
    
    
    if r.status_code == 200:
        if 'callback' in request.GET:
            xml_bytes = '%s(%s)' % (request.GET.get('callback'), r.text)
        else:
            xml_bytes = r.text
    else:
        xml_bytes = {'Response' : 'False'}
    
    return HttpResponse(xml_bytes, content_type='application/json; charset=utf-8')

def fiche(request, movie_id):
    try:
        moviepk = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("This Movie does not exist in your List")

    context = {
        'movie': moviepk,
    }
    return render(request, 'movies/fiche.html', context)

def manage(request):
    movies_list = Movie.objects.order_by('title')[:10]
    return render(request, 'movies/manage.html', {'movies_list': movies_list,})

def wanted(request):
    movies_list = Movie.objects.order_by('title')[:10]
    return render(request, 'movies/wanted.html', {'movies_list': movies_list,})

def search(request, movieName):

    return HttpResponse(xml_bytes, content_type='application/json; charset=utf-8')