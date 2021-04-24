from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
from .serializers import PizzaSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PizzaListCreateView(ListCreateAPIView):
    """Handles List and Create of a Pizza object"""
    queryset            = Pizza.objects.all()
    serializer_class    = PizzaSerializer
    

class PizzaUpdateRetriveDeleteView(RetrieveUpdateDestroyAPIView):
    """Handles update, retrive and delete of Pizza obj"""
    queryset            = Pizza.objects.all()
    serializer_class    = PizzaSerializer


   