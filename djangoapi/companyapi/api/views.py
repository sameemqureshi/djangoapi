from django.shortcuts import render
from api.models import Company,Machine
from rest_framework import viewsets
from api.serializers import CompanySerializer,MachineSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    @action(detail=True,methods=['get'])
    def machines(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            machines=Machine.objects.filter(company=company)
            machine_serializer=MachineSerializer(machines,many=True,context={'request':request})
            return Response(machine_serializer.data)
        except Exception as e:
            print(e)
        return Response({
            'message':'Company may not exist'
        })


class MachineViewSet(viewsets.ModelViewSet):
    queryset=Machine.objects.all()
    serializer_class=MachineSerializer