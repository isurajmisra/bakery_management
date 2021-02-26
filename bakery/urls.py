from django.urls import path
from .RestAPIs import *


urlpatterns = [
    path('users/register/', UserCreate.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_details'),
    path('products/add/', ProductCreate.as_view(), name='add_product'),
    path('products/', ProductView.as_view(), name='products'),
    path('products/update/<int:pk>/', ProductView.as_view(), name='products'),##Admin can update the details of the product i.e Add discount
    path('products/<int:pk>/', ProductDetail.as_view(), name='products'),
    path('products/ingredients/', IngredientsList.as_view(), name='ingredients'),
    path('products/ingredients/add/', IngredientsView.as_view(), name='add_ingredients'),
    path('products/ingredients/<int:pk>/', IngredientsDetail.as_view(), name='ingredients_details'),
    path('users/orders/create/', OrderCreate.as_view(), name='orders'),
    path('users/orders/history/', OrderHistory.as_view(), name='orders_history'),

]
