from django.shortcuts import render, redirect
from products.models import Products
from products.forms import Products_form
from django.views.generic import  DetailView,  DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
# Create your views here.


def menu_products(request):
    return render(request, 'menu_products.html')


def see_products(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'see_products.html', context = context)

   
class Create_products(CreateView, LoginRequiredMixin):
    model = Products
    template_name = 'create_products.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail-products', kwargs={'pk':self.object.pk})

        

class Delete_products(DeleteView, LoginRequiredMixin):
    model = Products
    template_name = "delete_products.html"
    def get_success_url(self):
        return reverse('see-products')

    
class Detail_products(DetailView):
    model = Products
    template_name= 'detail_products.html'
    

class Update_products(UpdateView):
    model = Products
    template_name = 'update_products.html'
    fields = 'Nombre', 'Precio', 'Categoria', 'Marca','SKU','Cantidad'


    def get_success_url(self):
        return reverse('detail-products', kwargs = {'pk':self.object.pk})
