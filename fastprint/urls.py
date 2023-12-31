"""
URL configuration for fastprint project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from apps import views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    
    # root
    path('', views.get_products_list_by_filter, name='get_products_list_by_filter'),
      
    # products
    path('api/v1/products/', views.get_products_list, name='get_products_list'),
    path('api/v1/products/post/', views.create_product, name='create_product'),
    path('api/v1/products/<int:pk>/', views.delete_product),
    path('api/v1/products/update/<int:pk>/', views.update_product, name='update_product'),
    path('api/v1/products/detail/<int:pk>/', views.get_detail_product),
        
    # categorys
    path('api/v1/categorys/', views.get_category_list),
    path('api/v1/categorys/post/', views.create_category),
    
    # status
    path('api/v1/status/', views.get_status_list),
]
