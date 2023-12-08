from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Produk, Kategori, Status
from sentry_sdk import capture_exception
from .serializers import (CreateProductSerializer, ViewsProductSerializer, CategorySerializer, StatusSerializer)

# get product list
@api_view(['GET'])
def get_products_list(request):

    try:

        products = Produk.objects.all().order_by('id_produk')
        serializer = ViewsProductSerializer(products, many=True)
        return JsonResponse({'data': serializer.data, 'message': 'success', 'error': None, 'status': 200}, safe=False)

    except Exception as e:
        return Response({'message': 'error', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# get detail product
@api_view(['GET'])
def get_detail_product(request, pk):

    try:

        detail = get_object_or_404(Produk, pk=pk)
        serializer = ViewsProductSerializer(detail)
        return Response({'data': serializer.data, 'message': 'success', 'error': 'null', 'status': 200}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'message': 'error', 'error': str(e), 'status': 500}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# create an product
@api_view(['POST'])
def create_product(request):

    if request.method == 'POST':

        try:

            serializer = CreateProductSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'message': 'success', 'error': None, 'status': 201}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            capture_exception(e)
            return Response({'message': 'error', 'error': str(e), 'status': 500}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({'message': 'invalid method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# delete an product
@api_view(['DELETE'])
def delete_product(request, pk):

    if request.method == 'DELETE':

        try:

            product = get_object_or_404(Produk, pk=pk)
            product.delete()
            return Response({'message': 'success', 'error': None, 'status': 204}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            capture_exception(e)
            return Response({'message': 'error', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({'message': 'invalid method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# update an product
@api_view(['PUT'])
def update_product(request, pk):

    if request.method == 'PUT':

        try:

            product = get_object_or_404(Produk, pk=pk)
            serializer = CreateProductSerializer(product, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data, 'message': 'success', 'error': None, 'status': 200}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            capture_exception(e)
            return Response({'message': 'error', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        return Response({'message': 'invalid method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

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
