from .models import Employes
from .serializers import EmployesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404



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
        
class Employes_details(APIView):

    def get_object(self, pk):
        try:
            return Employes.objects.get(pk=pk)
        except Employes.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):

        employe = self.get_object(pk)
        serializer = EmployesSerializer(employe)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):

        employe = self.get_object(pk)
        serializer = EmployesSerializer(employe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):

        employe = self.get_object(pk)
        employe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)