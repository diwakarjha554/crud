from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response 
from rest_framework import status
from authentication.serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from authentication.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken

# Generating the token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# User Registration
@api_view(['POST'])
@renderer_classes([UserRenderer])
def userRegistration(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({
            'token' : token,
            'msg': 'Registration success'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Login
@api_view(['POST'])
@renderer_classes([UserRenderer])
def userLogin(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({
                'token' : token,
                'msg': 'Login success'
            }, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


