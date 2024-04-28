from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics, mixins

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    