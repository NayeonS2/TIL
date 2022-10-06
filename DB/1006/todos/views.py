from re import L
from django.shortcuts import render
from .models import Todo
from .forms import TodoForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe



# Create your views here.

@require_safe
def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    todos = Todo.objects.all()
    context = {
        'todos':todos,
    }
    return render(request, 'todos/index.html', context)


@require_http_methods(['GET','POST'])
def new(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/new.html', context)


