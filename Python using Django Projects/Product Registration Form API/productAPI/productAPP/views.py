from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from productAPP.models import Product
from productAPP.serializers import ProductSerializer
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def product(request,type=""):
    if request.method=="POST":
        pro_json=JSONParser().parse(request)
        pro_serializer= ProductSerializer(data=pro_json)
        if pro_serializer.is_valid():
           pro_serializer.save()
           return JsonResponse("Product Add Successfully",safe=False)
        return JsonResponse("Product Not Add Successfully",safe=False)
        
    elif request.method=="PUT":
        pro_json=JSONParser().parse(request)
        prod=Product.object.get(productid=id)
        pro_serializer= ProductSerializer(prod,data=pro_json)
        if pro_serializer.is_valid():
            pro_serializer.save()
            return JsonResponse("Product Add Successfully",safe=False)
        return JsonResponse("Product Not Add Successfully",safe=False)
    
    elif request.method=="GET":
        prod=Product.objects.filter(type="cloths")
        pro_serializer= ProductSerializer(prod,many=True)
        return JsonResponse(pro_serializer.data,safe=False)
           
    elif request.method=="DELETE":
        prod=Product.objects.get(productid=id)
        prod.delete()
        return JsonResponse("Delete Successfully",safe=False)

def __str__(self):
        return self.productid +" "+ self.name