from django.urls import path, include
from .views import ProductList

app_name = 'products'
urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    #path('<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]