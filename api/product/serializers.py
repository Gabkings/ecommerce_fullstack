from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    images = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True,required=False)
    class Meta:
        model = Product
        fields = ("name","price","description","is_active","stock","category","images")