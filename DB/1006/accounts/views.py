from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm

# Create your views here.

@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('todos:index')
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'todos:index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)



def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('todos:index')




@require_http_methods(['GET','POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('todos:index')

    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
