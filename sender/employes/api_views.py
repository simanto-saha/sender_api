from django.shortcuts import render
from .models import Employes
from .serializers import EmployesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView



class Employes_list(APIView):

    def get(self, request):

        employes = Employes.objects.all()
        serialzer = EmployesSerializer(employes, many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)
    
    def post(self, request):

        serialzer = EmployesSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_200_OK)
        else:
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        