from rest_framework import serializers
from .models import Employes


class EmployesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employes
        fields = ['emp_id', 'emp_name', 'disgination']
