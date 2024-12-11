from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.decorators import api_view
from appCliente.models import cliente
from appConcierto.models import Concierto
from appEntrada.models import Entrada
from appApi.serializers import ClienteSerializer,ConciertoSerializer,EntradaSerializer

# Create your views here.

class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer



class ConciertoListCreateView(generics.ListCreateAPIView):
    queryset = Concierto.objects.all()
    serializer_class = ConciertoSerializer

class ConciertoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Concierto.objects.all()
    serializer_class = ConciertoSerializer



class EntradaListCreateView(generics.ListCreateAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

class EntradaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer



@api_view(['GET'])
def EntradaxCliente(request,id_cliente):
    try:
        cliente = cliente.objects.get(pk=id_cliente)
    except cliente.DoesNotExist:
        return Response({"ERROR" : "No se encontro cliente"}, status=status.HTTP_404_NOT_FOUND)
    
    Entradas = cliente.entrada.all()
    serializer = EntradaSerializer(Entradas, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def EntradaxConcierto(request,id_concierto):
    try:
        Concierto = Concierto.objects.get(pk=id_concierto)
    except Concierto.DoesNotExist:
        return Response({"ERROR" : "No se encontro concierto"}, status=status.HTTP_404_NOT_FOUND)
    
    Entradas = Concierto.entrada.all()
    serializer = EntradaSerializer(Entradas, many = True)
    return Response(serializer.data)

