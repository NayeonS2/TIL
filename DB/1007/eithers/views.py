import re
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required

from .models import Either, Comment
from .forms import EitherForm, CommentForm
# Create your views here.
@require_safe
def index(request):
    eithers = Either.objects.all()
    context = {
        'eithers': eithers,
    }
    return render(request, 'eithers/index.html', context)

@require_safe
def detail(request, pk):
    either = Either.objects.get(pk=pk)

    comment_form = CommentForm()

    comments = either.comment_set.all()

    context = {
        'either': either,
        'comment_form': comment_form,
        'comments': comments,
    }

    return render(request, 'eithers/detail.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = EitherForm(request.POST)
        if form.is_valid():
            either = form.save()
            return redirect('eithers:detail', either.pk)
    else:
        form = EitherForm()
    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)



@require_POST
def comments_create(request, pk):

    either = Either.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) # 저장하기 전에 뭐 더 할게 있는지 한번 더 기회를 줌 인스턴스를 반환
        comment.either = either # CommentForm에서 article 필드를 exclude시켰기때문에 is_valid() 검사안하고, 다른 방식으로 가져오게됨
        comment.save()

    return redirect('eithers:detail', either.pk)
