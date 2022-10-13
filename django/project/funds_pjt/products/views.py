from django.shortcuts import render
#import pandas as pd
#import numpy as np
#from sklearn.metrics.pairwise import cosine_similarity
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Product
from .forms import ProductForm
# Create your views here.
#funds = pd.read_csv('funds.csv')

@require_safe
def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST) 
        if form.is_valid():
            # 작성자를 저장하기 위해 commit = False
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('product:detail', product.pk)
    else:
        form = ProductForm()
    # print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'products/create.html', context)


@require_safe
def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
  
    context = {
        'product': product,
        # 반드시 html에서 사용할 수 있도록 comment_form을 전달해야 함
       
    }
    return render(request, 'products/detail.html', context)


@require_POST
def delete(request, pk):
    product = get_object_or_404(product, pk=pk)
    # 글쓴이가 아닌 사람이 삭제하려고 하는 것을 방지
    if request.user != product.user:
        return redirect('products:detail', product.pk)

    if request.user.is_authenticated:
        product.delete()

    return redirect('products:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    product = get_object_or_404(product, pk=pk)

    # 글쓴이가 아닌 사람이 수정하려고 하는 것을 방지
    if request.user != product.user:
        return redirect('products:detail', product.pk)

    if request.method == 'POST':
        # Create a form to edit an existing product,
        # but use POST data to populate the form.
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:detail', product.pk)
    else:
        # Creating a form to change an existing product.
        form = ProductForm(instance=product)
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'products/update.html', context)
