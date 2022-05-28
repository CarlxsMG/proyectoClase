# Django imports
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Third party imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Local imports
from .serializers import LoginSerializer
from .models import SellerUser, BuyerUser, ManagementUser


# Views.
def user_login(request, user_type):
    data = {}
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        email_ser = serializer.data['email']
        password = serializer.initial_data['password']

        try:
            if user_type == 'S':
                user = SellerUser.objects.get(email=email_ser)
            elif user_type == 'B':
                user = BuyerUser.objects.get(email=email_ser)
            elif user_type == 'M':
                user = ManagementUser.objects.get(email=email_ser)
            else:
                raise 
            
            data['email'] = user.email
            data['user_id'] = user.id
        except Exception as e:
            raise 

        token = Token.objects.get_or_create(user=user)[0].key
        data["token"] = 'Token ' + token

        if not authenticate(email=email_ser, password=password):
            raise

        login(request, user)

        data["message"] = 'User loged in successfully'
    
        return Response(data, status=status.HTTP_200_OK)
    else:
        
        data = serializer.errors   
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

def user_logout(request):

    data = {}
    request.user.auth_token.delete()

    logout(request)

    data['message'] = 'User logged out'

    return Response(data, status=status.HTTP_200_OK)