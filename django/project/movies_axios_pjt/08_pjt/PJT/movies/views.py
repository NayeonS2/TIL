from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie, Genre


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        "movies" : movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)    
    genres_list = []
    genresid = list(movie.genres.values())

    for genreid in genresid:
        genres_list.append(genreid['name'])
 
        
    context = {
        "movie" : movie,
        'genres_list': genres_list,
        'genresid': genresid,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    movies = Movie.objects.all()
    recommended_list = []

    i = 1
    for movie in movies:
        
        genres_list = []
        genresid = list(movie.genres.values())
        for genreid in genresid:
            genres_list.append(genreid['name'])
        if int(str(movie.release_date)[:4]) < 1990 and ("드라마" in genres_list or "로맨스" in genres_list):
            recommended_list.append([str(i),movie.title, movie.vote_average, str(movie.release_date),movie.poster_path])
            i += 1
    context = {
        'recommended_list' : recommended_list[:10],
    }
    return render(request, 'movies/recommended.html', context)