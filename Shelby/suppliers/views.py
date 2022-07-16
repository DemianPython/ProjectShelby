from django.shortcuts import render, redirect
from .forms import Suppliers_form, OrderProducts_form
from .models import Suppliers, OrderProducts
# Create your views here.

def suppliers(request):
    return render(request, 'menu_suppliers.html', context={})

def see_suppliers(request):
    suppliers = Suppliers.objects.all()
    context = {'suppliers':suppliers}
    return render(request, 'see_suppliers.html', context = context)



def create_suppliers(request):
    if request.method == 'GET':
        form_supplier = Suppliers_form()
        context = {'form_supplier':form_supplier}
        return render(request, 'create_suppliers.html', context=context)
    else:
        form = Suppliers_form(request.POST)
        if form.is_valid():
            new_supplier = Suppliers.objects.create(
                Nombre = form.cleaned_data['Nombre'],
                Productos = form.cleaned_data['Productos'],
                Debe = form.cleaned_data['Debe'],
                Haber = form.cleaned_data['Haber'],     
            )
            context ={'new_supplier':new_supplier}
        return redirect('/see-suppliers')


def create_Order_Products(request):
    if request.method == 'GET':
        form_OrderProducts = OrderProducts_form()
        context = {'form_OrderProducts':form_OrderProducts}
        return render(request, 'create_OrderProducts.html', context=context)
    else:
        form = OrderProducts_form(request.POST)
        if form.is_valid():
            new_OrderProducts = OrderProducts.objects.create(
                Empresa = form.cleaned_data['Empresa'],
                Lista_de_productos  = form.cleaned_data['Lista_de_productos'],
                Fecha_de_pedido  = form.cleaned_data['Fecha_de_pedido'],
                Fecha_de_entrega = form.cleaned_data['Fecha_de_entrega'],
                Total = form.cleaned_data['Total'],      
            )
            context ={'new_OrderProducts':new_OrderProducts}
        return redirect('/see-order')


def see_OrderProducts(request):
     Orderproducts = OrderProducts.objects.all()
     context = {'Orderproducts':Orderproducts}
     return render(request, 'see_OrderProducts.html', context = context)