from rest_framework import serializers
from PizzaApi import models


class PizzaSerializer(serializers.ModelSerializer):
    """Serializer for Pizza """
    pizza_size = serializers.ListField()
    pizza_toppings = serializers.ListField()
    class Meta:
        model       = models.Pizza
        fields      = ("__all__")