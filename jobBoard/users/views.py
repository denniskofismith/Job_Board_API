from django.shortcuts import render
from rest_framework import generics,permissions,status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView

User = get_user_model()

# Create your views here.

class RegisterView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    
    def post(self,request,*args,**kwargs):
        username= request.data.get("username")
        password = request.data.get("password")
        user = User.objects.filter(username=username).first()
        
        if user and user.check_password(password):
            
            refresh = RefreshToken.for_user(user)
            
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data
            })
        return Response({'error':'Invalid Credentials'},status=status.HTTP_401_UNAUTHORIZED)
    
    
class ProfileView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request):
        return Response({"message": f"hello {request.user.username}"})
