import logging
from multiprocessing import Pool

from django.shortcuts import render
from .forms import ProductsAddForm
from .forms import ProductDetailForm

from main.models import Product
from main.product_scrapper import save_scrapped_data

logger = logging.getLogger('django')


def product_list(request):
    return render(request, "product_list.html", {'products': Product.objects.all()})


def add_product(request):
    form = ProductsAddForm(request.POST)
    context = {'form': form}

    if form.is_valid():
        product_ids = form.cleaned_data.get('product_ids', '').split(' ')

        pool = Pool()
        print(pool.map(save_scrapped_data, product_ids))

        context['started'] = True
        context['product_ids'] = product_ids

    return render(request, "product_add.html", context)


def product_detail(request):
    context = {'form': ProductDetailForm(request.POST)}

    product_id = request.POST.get('product_id', None)
    if product_id:
        product = Product.objects.filter(pk=product_id).first()
        context.update({
            'product': product,
            'has_result': True,
        })

    return render(request, "product_detail.html", context)
