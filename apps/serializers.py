from rest_framework import serializers
from .models import Kategori, Produk, Status

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produk
        fields=['id_produk', 'nama_produk', 'harga', 'kategori', 'status', 'created_at', 'updated_at',]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Kategori
        fields=['nama_kategori']
        
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Status
        fields=['nama_status']