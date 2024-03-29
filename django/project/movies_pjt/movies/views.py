from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseForbidden

from .models import Movie
from .forms import MovieForm
# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)


@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

@require_safe
def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)
   
@login_required
@require_http_methods(['GET','POST'])
def update(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)

            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:index')
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)
    



@require_POST
def delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == movie.user:
            movie.delete()
            return redirect('movies:index')
        return HttpResponseForbidden
    return HttpResponse(status=401)

