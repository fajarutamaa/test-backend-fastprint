from rest_framework import serializers
from .models import (Kategori, Produk, Status)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['nama_kategori']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['nama_status']


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = ['id_produk', 'nama_produk', 'harga',
                  'kategori', 'status', 'created_at', 'updated_at']


class ViewsProductSerializer(serializers.ModelSerializer):
    kategori = CategorySerializer()
    status = StatusSerializer()

    class Meta:
        model = Produk
        fields = ['id_produk', 'nama_produk', 'harga',
                  'kategori', 'status', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['kategori'] = representation['kategori']['nama_kategori']
        representation['status'] = representation['status']['nama_status']
        return representation
