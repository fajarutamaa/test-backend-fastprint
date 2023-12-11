from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import sweetify
from apps.forms import ProdukForm
from .models import Produk, Kategori, Status
from sentry_sdk import capture_exception
from .serializers import (CreateProductSerializer, ViewsProductSerializer, CategorySerializer, StatusSerializer)

# get product list
@api_view(['GET'])
def get_products_list(request):

    try:
        products = Produk.objects.all().order_by('id_produk')
        serializer = ViewsProductSerializer(products, many=True)
        return render(request, 'dashboard.html', {'products': products})
        return JsonResponse({'data': serializer.data, 'message': 'success', 'error': None, 'status': 200}, safe=False)
    except Exception as e:
        return Response({'message': 'error', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def get_products_list_by_filter(request):

    try:
        products = Produk.objects.all().order_by('id_produk').filter(status='1')
        serializer = ViewsProductSerializer(products, many=True)
        return render(request, 'index.html', {'products': products})
        return JsonResponse({'data': serializer.data, 'message': 'success', 'error': None, 'status': 200}, safe=False)
    except Exception as e:
        return Response({'message': 'error', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# get detail product
def get_detail_product(request, pk):
    try:
        detail = get_object_or_404(Produk, pk=pk)
        serializer = ViewsProductSerializer(detail)
        return Response({'data': serializer.data, 'message': 'success', 'error': 'null', 'status': 200}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'message': 'error', 'error': str(e), 'status': 500}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# create an product
def create_product(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'data produk berhasil ditambahkan')
            return redirect('/api/v1/products/')
    else:
        form = ProdukForm()

    return render(request, 'add_product.html', {'form': form})

# delete an product
def delete_product(request, pk):
        try:
            product = get_object_or_404(Produk, pk=pk)
            product.delete()
            return redirect('/api/v1/products/')
        
        except Exception as e:
            capture_exception(e)
            return Response({'message': 'error', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# update an product
def update_product(request, pk):
    product = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'data produk berhasil ditambahkan', timer=2000)
            return redirect('/api/v1/products/', pk=pk)
          
    else:
            form = ProdukForm(instance=product)
            
    return render(request, 'edit.html', {'product': product,'form':form})
        
        
# get category list
@api_view(['GET'])
def get_category_list(request):

    try:

        categorys = Kategori.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return JsonResponse({'data': serializer.data, 'message': 'success', 'error': None, 'status': 200}, safe=False)

    except Exception as e:
        capture_exception(e)
        return Response({'message': 'error', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# create an category
@api_view(['POST'])
def create_category(request):

    if request.method == 'POST':

        try:

            serializer = CategorySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'message': 'success', 'error': None, 'status': 201}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            capture_exception(e)
            return Response({'message': 'error', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({'message': 'invalid method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# get status list
@api_view(['GET'])
def get_status_list(request):

    try:

        status = Status.objects.all()
        serializer = StatusSerializer(status, many=True)
        return JsonResponse({'data': serializer.data, 'message': 'success', 'error': None, 'status': 200}, safe=False)

    except Exception as e:
        capture_exception(e)
        return Response({'message': 'error', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
