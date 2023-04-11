from django.shortcuts import render
from .models import Details
from .serializers import DetailSerializers
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def details(request,name=" "):
    if request.method=="POST":
        detail_parser=JSONParser().parse(request)
        detail_serializers=DetailSerializers(data=detail_parser)
        if detail_serializers.is_valid():
            detail_serializers.save()
            return JsonResponse("Add Successfully",safe=False)
        return JsonResponse("Error to Add",safe=False)
    elif request.method=="PUT":
        detail_parser=JSONParser().parse(request)
        detail_data=Details.objects.get(name=name)
        detail_serializers=DetailSerializers(detail_data,data=detail_parser)
        if detail_serializers.is_valid():
            detail_serializers.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Error to Update",safe=False)
    elif request.method=="GET":
        detail_data=Details.objects.get(name=name)
        detail_serializers=DetailSerializers(data=detail_data)
        return JsonResponse(detail_serializers,safe=False)
    elif request.method=="DELETE":
        detail_data=Details.objects.get(id=id)
        detail_serializers=DetailSerializers(data=detail_data)
        detail_serializers.delete()
        return JsonResponse("Delete Successfully",safe=False)



