from django.shortcuts import redirect, render
from appCliente.models import cliente
from appCliente.form import FormCliente


# Create your views here.


def lista(request):
    i = cliente.objects.all()
    data = {'cliente':i}
    return render(request, 'appCliente/lista.html', data)

def agregar(request):
    form = FormCliente
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
            return lista(request)
    else:
        form= FormCliente()

    data = {'form':form}
    return render(request, 'appCliente/agregar.html', data)

def editar(request,id):
    icliente = cliente.objects.get(id=id)
    form = FormCliente (instance=icliente)
    if request.method == 'POST':
        form = FormCliente(request.POST, instance=icliente)
        if form.is_valid():
            form.save()
            return lista(request)
    else:
        form= FormCliente(instance=icliente)

    data = {'form':form}
    return render(request, 'appCliente/agregar.html', data)

def eliminar(request,id):
    icliente = cliente.objects.get(id=id)
    icliente.delete()
    return redirect('lista')