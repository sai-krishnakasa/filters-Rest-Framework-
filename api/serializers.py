from .models import students
from rest_framework import serializers

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=students
        fields='__all__' 
        