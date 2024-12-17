from django.contrib import admin
from django.urls import path

from appEntrada import views as Entrada
from appCliente import views as Cliente
from appConcierto import views as Concierto
from appApi import views as Api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Entrada.index),

    # Rutas de la App Cliente

    path('Cliente/lista/', Cliente.lista, name='lista'),
    path('Cliente/agregar/', Cliente.agregar, name='agregar'),
    path('Cliente/editar/<int:id>/', Cliente.editar, name='editar'),
    path('Cliente/eliminar/<int:id>/', Cliente.eliminar, name='eliminar'),

    # Rutas de App Concierto

    path('Concierto/conciertos/', Concierto.listadoConcierto, name='listadoConcierto'),
    path('Concierto/agregarConcierto/', Concierto.agregarConcierto),
    path('Concierto/actualizarConcierto/<int:id>', Concierto.actualizarConcierto),
    path('Concierto/eliminarConcierto/<int:id>', Concierto.eliminarConcierto),

    # Rutas de la App Entrada
    path('Entrada/lista/', Entrada.lista_entradas, name='listaEntrada'),
    path('Entrada/agregar/', Entrada.agregar_entrada),
    path('Entrada/editar/<int:id>', Entrada.editarEntrada),
    path('Entrada/eliminar/<int:id>', Entrada.eliminarEntrada),

    # Api Rest
    #Urls de la Api Cliente 
    path('Api/Cliente/', Api.ClienteListCreateView.as_view(), name='apiclientes'),
    path('Api/Cliente/<int:pk>/', Api.ClienteRetrieveUpdateDestroyView.as_view(), name='cliente'),
    path('Api/Cliente/<int:id_cliente>/Entrada/', Api.EntradaxCliente, name='entradaxcliente'),
    
    #Urls de la Api Concierto
    path('Api/Concierto/', Api.ConciertoListCreateView.as_view(), name='apiconcierto'),
    path('Api/Concierto/<int:pk>/', Api.ConciertoRetrieveUpdateDestroyView.as_view(), name='concierto'),
    path('Api/Concierto/<int:id_concierto>/Entrada/', Api.EntradaxConcierto, name='entradaxconcierto'),

    #Urls de la Api Entrada
    path('Api/Entrada/', Api.EntradaListCreateView.as_view(), name='apientrada'),
    path('Api/Entrada/<int:pk>/', Api.EntradaRetrieveUpdateDestroyView.as_view(), name='entrada'),
]
