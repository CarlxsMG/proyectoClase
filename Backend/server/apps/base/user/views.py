# Django imports
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


# Third party imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

# Local imports
from .serializers import LoginSerializer
from .models import SellerUser, BuyerUser, ManagementUser


# Views.
@csrf_exempt
@api_view(['POST'])
def user_login(request, user_type):
    data = {}
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        username = serializer.data['username']
        password = serializer.initial_data['password']

        try:
            if user_type == 'S':
                user = SellerUser.objects.get(username=username)
            elif user_type == 'B':
                user = BuyerUser.objects.get(username=username)
            elif user_type == 'M':
                user = ManagementUser.objects.get(username=username)
            else:
                raise 
            
            data['email'] = user.email
            data['username'] = user.username
            data['user_id'] = user.id
        except Exception as e:
            raise 

        token = Token.objects.get_or_create(user=user)[0].key
        data["token"] = 'Token ' + token

        if not authenticate(username=username, password=password):
            raise

        login(request, user)

        data["message"] = 'User loged in successfully'
    
        return Response(data, status=status.HTTP_200_OK)
    else:
        
        data = serializer.errors   
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_logout(request):

    data = {}

    logout(request)

    data['message'] = 'User logged out'

    return Response(data, status=status.HTTP_200_OK)