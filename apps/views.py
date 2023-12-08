from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Produk, Kategori, Status
from .serializers import ProductSerializer, CategorySerializer, StatusSerializer

# Create your views here.
@api_view(['GET'])
def get_products_list(request):
    products = Produk.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse({'message': 'success','data':serializer.data}, safe=False)

@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, {'message': 'success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'message': 'invalid method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
     
@api_view(['DELETE'])
def delete_product(request, pk):
    if request.method == 'DELETE':
        product = get_object_or_404(Produk, pk=pk)
        product.delete()
        return Response({'message': 'success'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'message': 'invalid method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
@api_view(['PUT'])
def update_product(request, pk):
    if request.method == 'PUT':
        product = get_object_or_404(Produk, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, {'message': 'success'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'message': 'invalid method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
@api_view(['GET'])
def get_category_list(request):
    categorys = Kategori.objects.all()
    serializer = CategorySerializer(categorys, many=True)
    return JsonResponse({'message': 'success', 'data':serializer.data}, safe=False)

@api_view(['POST'])
def create_category(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, {'message': 'success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'message': 'invalid method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        

@api_view(['GET'])
def get_status_list(request):
    status = Status.objects.all()
    serializer = StatusSerializer(status, many=True)
    return JsonResponse({'message': 'success', 'data':serializer.data}, safe=False)
