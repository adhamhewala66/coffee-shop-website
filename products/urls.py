from django.urls import path, include
from .views import ProductList, ProductDetail, search

app_name = 'products'
urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('search/', search, name='search')
]
