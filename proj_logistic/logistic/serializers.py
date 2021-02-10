from rest_framework import serializers
from .models import Logistic

class LogisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logistic
        fields = '__all__'