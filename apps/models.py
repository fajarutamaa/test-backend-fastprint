from django.db import models
from django.utils import timezone

# Create your models here.
class Kategori(models.Model):
    nama_kategori= models.CharField(max_length=255)
    
    def __str__(self):
        return self.nama_kategori
        
class Status(models.Model):
    nama_status=models.CharField(max_length=255)
    
    def __str__(self):
        return self.nama_status

class Produk(models.Model):
    id_produk= models.AutoField(primary_key=True)
    nama_produk= models.CharField(max_length=255, null = False)
    harga= models.DecimalField(max_digits=10, decimal_places=2, null = False)
    kategori= models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status= models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at= models.DateTimeField(default=timezone.now)
    updated_at= models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nama_produk