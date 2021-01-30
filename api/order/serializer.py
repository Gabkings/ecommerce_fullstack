from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("user", "products", "total_products", "total_amount", "transaction_id", "created_at", "updated_at")

        