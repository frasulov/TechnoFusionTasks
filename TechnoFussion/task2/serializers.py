from .models import *
from rest_framework import serializers

class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = '__all__'

class SuppSeqSerializer(serializers.ModelSerializer):

    class Meta:
        model = SuppSeq
        fields = '__all__'

class LabelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Labels
        fields = '__all__'
