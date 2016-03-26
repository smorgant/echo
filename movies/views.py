from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

# Views here:
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

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
    context = {
        'movies_list': movies_list,
    }
    return render(request, 'movies/manage.html', context)

def wanted(request):
    response = "You're looking at the results of Wanted"
    return HttpResponse(response)