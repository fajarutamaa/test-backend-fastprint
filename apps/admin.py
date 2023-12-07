from django.contrib import admin
from .models import Kategori, Status, Produk

# Register your models here.
admin.site.register([Kategori, Status, Produk])