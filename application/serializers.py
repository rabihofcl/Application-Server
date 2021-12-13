from rest_framework import serializers
from .models import ApplicationForm



class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = "__all__"

class StatusChangeFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        exclude = ['logo']