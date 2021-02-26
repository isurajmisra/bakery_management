from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from ..Serializers import OrderSerializer, OrderHistorySerializer
from ..utiliy import get_total_price


class OrderCreate(generics.CreateAPIView):
    "Any user can create the order."
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            result = {
                "user": order.user.get_full_name(),
                "products": {
                },

            }
            for product in order.products.all():
                result['products']['name'] = product.name
                result['products']['price'] = product.selling_price
            for product in order.products_details['products']:
                if order.products.filter(id=int(product['id'])).first():
                    result['products']['quantity'] = product['quantity']
                else:
                    result['products']['quantity'] = 0

            result['total_price'] = get_total_price(order)
            order.total_price = get_total_price(order)
            order.save()
            return Response(data=result)


class OrderHistory(generics.ListAPIView):
    "Users can see their order history"
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    serializer_class = OrderHistorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.orders.all()
