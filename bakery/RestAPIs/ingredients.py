from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from ..models import Ingredient
from ..Serializers import IngredientsSerializer


class IngredientsView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = (permissions.IsAdminUser,)

#
class IngredientsList(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = (permissions.AllowAny,)


class IngredientsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = (permissions.IsAdminUser,)