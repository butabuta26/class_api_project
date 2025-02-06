from django.urls import path
from products.views import ProductListCreativeView, reviews_view, ProductDetailView

urlpatterns = [
    path('products/', ProductListCreativeView.as_view(), name="products"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('reviews/', reviews_view, name="reviews")
]