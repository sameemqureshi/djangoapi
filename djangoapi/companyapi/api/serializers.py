from rest_framework import serializers
from api.models import Company,Machine


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    comapny_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"

class MachineSerializer(serializers.HyperlinkedModelSerializer):
    machine_id=serializers.ReadOnlyField()
    class Meta:
        model=Machine
        fields="__all__"