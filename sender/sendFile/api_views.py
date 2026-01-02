from django.shortcuts import render
from .models import Userdetails
from .serializers import UserdetailsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET', 'POST'])
def userdetails_list(request):
    if request.method == 'GET':
        # get all the data 
        userDetail = Userdetails.objects.all()
        serializer = UserdetailsSerializer(userDetail, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = UserdetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def userdetails(request, pk):

    try:
        user = Userdetails.objects.get(pk=pk)
    except Userdetails.DoesNotExist:
        return Response(
            {"error": "User not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = UserdetailsSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = UserdetailsSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
