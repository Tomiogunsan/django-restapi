from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product
from django.forms.models import model_to_dict
from product.serializers import ProductSerializer
import json

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
       instance = serializer.save()
       return JsonResponse(serializer.data)