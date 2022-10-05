from ast import Delete
from re import A
from django.shortcuts import render
from .serializers import *
from .models import *
#rest framework
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


def home(request):
    return render(request, 'home.html')



# krasovka API
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def krosovkaMakeAPI(request):
    krosovka = Krosovka.objects.all()
    serializer = KrosovkaAPI(krosovka, many=True)
    return Response(serializer.data)


# krasovka APIni aloxida chiqarish

@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def singleAPI(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializer = KrosovkaAPI(krosovka, many=False)
    return Response(serializer.data)



# mashina API


@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def MashinaMakeAPI(request):
    mashina = Mashina.objects.all()
    serializer = MashinaAPI(mashina, many=True)
    return Response(serializer.data)


# krasovka APIni aloxida chiqarish


@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def bittaAPI(request, pk):
    mashina = Mashina.objects.get(id=pk)
    serializer = MashinaAPI(mashina, many=False)
    return Response(serializer.data)

# mahsulot API


@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def MahsulotMakeAPI(request):
    mahsulot = Mahsulot.objects.all()
    serializer = MashinaAPI(mahsulot, many=True)
    return Response(serializer.data)


# krasovka APIni aloxida chiqarish


@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def birAPI(request, pk):
    mahsulot = Mahsulot.objects.get(id=pk)
    serializer = MashinaAPI(mahsulot, many=False)
    return Response(serializer.data)



# post joylash POST malumot joylash

@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def malumotjoylash(request):
    serializer = MahsulotAPI(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)
    
    
# update post


@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def malumotyangilash(request, pk):
    mahsulot = Mahsulot.objects.get(id=pk)
    serializer = MahsulotAPI(instance=mahsulot, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)
    
    
    
# post delete


@api_view(["DELETE"])
@permission_classes((permissions.AllowAny, ))
def malumotdelete(request, pk):
    mahsulot = Mahsulot.objects.get(id=pk)
    mahsulot.delete()
        
    return Response("mufoqiyatli ochirildi")