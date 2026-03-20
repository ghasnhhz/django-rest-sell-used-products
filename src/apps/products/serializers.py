from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'seller', 'buyer', 'title', 'description', 'price', 'is_sold', 'created_at']
        read_only_fields = ['seller', 'buyer', 'is_sold', 'created_at']