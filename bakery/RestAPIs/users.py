from ..Serializers import UserSerializer, UserDetailSerializer
from ..models import User
from rest_framework import generics, viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication



class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)



class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
