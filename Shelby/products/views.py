from django.shortcuts import render, redirect
from products.models import Products
from products.forms import Products_form
# Create your views here.


def menu_products(request):
    return render(request, 'menu_products.html')


def see_products(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'see_products.html', context = context)

def create_products(request):
    if request.method == 'GET':
        form = Products_form()
        context = {'form':form}
        return render(request, 'create_products.html', context=context)
    else:
        form = Products_form(request.POST)
        if form.is_valid():
            new_product = Products.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                category = form.cleaned_data['category'],
                SKU = form.cleaned_data['SKU'],
                quantity = form.cleaned_data['quantity'],
            )
            context ={'new_product':new_product}
        return redirect('/see-products')