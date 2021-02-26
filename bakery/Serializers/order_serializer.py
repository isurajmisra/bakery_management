from rest_framework import serializers
from ..models import Order
from .products_serializer import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("user", "products", "products_details")


class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
