from django.shortcuts import render, redirect
from .models import Clients
from .forms import Clients_form
# Create your views here.
def client(request):
    return render(request, 'menu_client.html')

def create_client(request):
    if request.method == 'GET':
        form_client = Clients_form()
        context = {'form_client':form_client}
        return render(request, 'create_client.html', context=context)
    else:
        form = Clients_form(request.POST)
        if form.is_valid():
            new_client = Clients.objects.create(
                Nombre_del_cliente = form.cleaned_data['Nombre_del_cliente'],
                Nombre_del_local = form.cleaned_data['Nombre_del_local'],
                Localidad = form.cleaned_data['Localidad'],
                Direccion_del_local = form.cleaned_data['Direccion_del_local'],
                Cuenta_corriente = form.cleaned_data['Cuenta_corriente'],
            )
            context ={'new_client':new_client}
        return redirect('/see-client')

def see_client(request):
    client = Clients.objects.all()
    context = {'client':client}
    return render(request, 'see_client.html', context = context)