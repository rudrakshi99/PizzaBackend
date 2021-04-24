from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza, pizza_size_choices, pizza_toppings_choices
from .serializers import PizzaSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response

class PizzaListCreateView(ListCreateAPIView):
    """Handles List and Create of a Pizza object"""
    queryset            = Pizza.objects.all()
    serializer_class    = PizzaSerializer
    
    filter_backends     = [DjangoFilterBackend]
    filterset_fields    = ('__all__')
        
    def create(self, request):
        serializer = PizzaSerializer(data=request.data)  # convert complex data by passing into serializer
        if serializer.is_valid():                        # check for validation of data
            new_size     = request.data['pizza_size']
            new_toppings = request.data['pizza_toppings']
        
            limit2 = len(pizza_size_choices)+1
            limit3 = len(pizza_toppings_choices)+1            
           
            for s in new_size:
                if int(s) > limit2 or int(s)==0:
                    return Response({"error":"Invalid choice"}, status=status.HTTP_400_BAD_REQUEST)  # return error for invalid data  
            for s in new_toppings or int(s)==0:
                if int(s) > limit3:
                    return Response({"error":"Invalid choice"}, status=status.HTTP_400_BAD_REQUEST)  # return error for invalid data
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    # return http satuts 201 when post is created successfully
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # return error for invalid data
  
   


class PizzaUpdateRetriveDeleteView(RetrieveUpdateDestroyAPIView):
    """Handles update, retrive and delete of Pizza obj"""
    queryset            = Pizza.objects.all()
    serializer_class    = PizzaSerializer
    lookup_field        = 'id'                                      # comparing through id
    
    def retrieve(self, request, pk ):
        try:                                                        # check if Pizza exist
            pizza = Pizza.objects.get(id=pk)
        except Pizza.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)   # return http status 404 if Pizza doesn't exist
        
        serializer = PizzaSerializer(pizza)                         # convert complex data by passing into serializer
        return Response(serializer.data)                            # return the JSON response
    
    
    def patch(self, request, pk):
        try:                                                        # check if Pizza exist
            pizza = Pizza.objects.get(id=pk)                          
        except Pizza.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)   # return http status 404 if Pizza doesn't exist   
       
        serializer = PizzaSerializer(pizza, data=request.data)      # convert complex data by passing into serializer 
                                                                    # but make name as 'read ony field's    
        if serializer.is_valid():                                   # check for validation of data
          
            new_size = request.data['pizza_size']
            new_toppings = request.data['pizza_toppings']
        
            limit2 = len(pizza_size_choices)+1
            limit3 = len(pizza_toppings_choices)+1            
           
            for s in new_size:
                if int(s) > limit2 or int(s)==0:
                    return Response({"error":"Invalid choice"}, status=status.HTTP_400_BAD_REQUEST)  # return error for invalid data  
            for s in new_toppings or int(s)==0:
                if int(s) > limit3:
                    return Response({"error":"Invalid choice"}, status=status.HTTP_400_BAD_REQUEST)  # return error for invalid data
                 
            serializer.save()
            return Response(serializer.data)                                    # return updated the JSON response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # return error for invalid data
       
     
    
    def delete(self, request, pk):
        try:                                                        # check if Pizza exist
            pizza = Pizza.objects.get(id=pk)
        except Pizza.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)   # return http status 404 if Pizza doesn't exist
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)          # return http status 204 
