from dataclasses import field
from pyexpat import model
from .models import Krosovka, Mashina, Mahsulot
from rest_framework import serializers


class KrosovkaAPI(serializers.ModelSerializer):
    class Meta:
        model = Krosovka
        fields = '__all__'
        
        
        
class MashinaAPI(serializers.ModelSerializer):
    class Meta:
        model = Mashina
        fields = '__all__'
        
        
class Mahsulot(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'