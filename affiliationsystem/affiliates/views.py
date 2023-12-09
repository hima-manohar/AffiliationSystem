
from django.shortcuts import render, redirect
from .models import Product, Affiliate, Sale
from .forms import SaleRecordForm
from django.shortcuts import get_object_or_404

def product_list(request):
    products = Product.objects.all()
    return render(request, 'affiliates/product_list.html', {'products': products})

def register_affiliate(request):
    if request.method == 'POST':
       
        return redirect('product_list')
    else:
     
        return render(request, 'affiliates/register_affiliate.html')


def record_sale(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = SaleRecordForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.product = product
            sale.save()
            return redirect('product_list')
    else:
        form = SaleRecordForm()

    return render(request, 'affiliates/record_sale.html', {'product': product, 'form': form})


