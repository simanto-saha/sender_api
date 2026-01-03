from rest_framework import serializers
from .models import Employes
from sendFile.models import Userdetails


class EmployesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employes
        fields = ['emp_id', 'emp_name', 'disgination']

class Userdetailsserializer(serializers.ModelSerializer):

    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Userdetails
        fields = ['user','file', 'file_url', 'email']

    def get_file_url(self, obj):
        if obj.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.file.url)
        return None
