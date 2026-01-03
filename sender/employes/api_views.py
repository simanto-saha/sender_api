from .models import Employes, APIKey
from sendFile.models import Userdetails
from .serializers import EmployesSerializer, Userdetailsserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


#class Base api
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
        


#api class      
class Employes_details(APIView):

    def get(self, request):
        # Query 
        employe_id = request.query_params.get('id')
        api_key = request.query_params.get('appid')

        # Validate id first
        if not employe_id:
            return Response({"error": "Employe ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Validate api_key
        if not api_key:
            return Response({"error": "API Key is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Convert to int safely
        try:
            employe_id = int(employe_id)
        except ValueError:
            return Response({"error": "Invalid Employee ID format."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Only 3 employees can show
        #if employe_id > 3:
            #return Response({"error": "You are not authorised"}, status=status.HTTP_403_FORBIDDEN)
        
        # Check api_key valid
        try:
            api_key_obj = APIKey.objects.get(key=api_key, is_active=True)
        except APIKey.DoesNotExist:
            return Response({"error": "Invalid or inactive API Key."}, status=status.HTTP_403_FORBIDDEN)
        
        # Fetch employe details
        try:
            employe = Employes.objects.get(emp_id=employe_id)
            user = Userdetails.objects.filter(user=employe_id).first()  # Changed here
            
            if not user:
                return Response({"error": "User details not found."}, status=status.HTTP_404_NOT_FOUND)
                
        except Employes.DoesNotExist:
            return Response({"error": "Employe not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize and return data
        serializer = EmployesSerializer(employe)
        serializer2 = Userdetailsserializer(user, context={'request': request})

        combined_data = {
            "employes": serializer.data,
            "userdetails": serializer2.data
        }

        return Response(combined_data, status=status.HTTP_200_OK)
    
        
    #First fetch the data using function
    """def get_object(self, pk):
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
        return Response(status=status.HTTP_204_NO_CONTENT)"""