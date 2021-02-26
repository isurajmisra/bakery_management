from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from ..models import Product, Order
from ..Serializers import ProductSerializer


class ProductView(generics.ListAPIView):
    '''
    Users can view all products.
    '''
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProductCreate(generics.ListCreateAPIView):
    '''
    Admin can add new products.
    '''
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAdminUser,)


class ProductUpdate(generics.RetrieveUpdateDestroyAPIView):
    '''
    Admin can update any product details.
    '''
    authentication_classes = [SessionAuthentication,]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAdminUser,)


class ProductDetail(generics.RetrieveAPIView):
    '''
    User can see the details of the product.
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)


# class HotSellingProducts(generics.ListAPIView):
#     serializer_class = ProductSerializer
#     permission_classes = (permissions.IsAdminUser,)
#
#     def get_queryset(self):
#         products = Product.objects.all()
#         for prod in products:
#             prod.products_order.all().aggregate(Sum(''))
#         Order.ojects.filter()