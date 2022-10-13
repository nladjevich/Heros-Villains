from pyexpat import model
from rest_framework import serializers
from .models import SuperType, Supers

class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type']
        depth = 1