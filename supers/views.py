from django.shortcuts import render
from .serializers import SupersSerializer
from .models import Supers
from supers import serializers
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def supers_list(request):

    if request.method == 'GET':
        super = Supers.objects.all()
        super_type1 = request.query_params.get('supertype')
        super_hero = Supers.objects.filter(super_type=1).values()
        super_villain = Supers.objects.filter(super_type=2).values()
        hero_serializer = SupersSerializer(super_hero, many=True)
        villain_serializer = SupersSerializer(super_villain, many=True)

        custom_dict = {
            'Heroes': hero_serializer.data ,
            'Villains': villain_serializer.data ,
        }

        if super_type1:
            super = super.filter(super_type__type=super_type1)
            
        serializer = SupersSerializer(super, many=True)
        return Response(custom_dict)

    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
