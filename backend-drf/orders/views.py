from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from carts.models import Cart, CartItem
from .models import Order, OrderItem


class PlaceOrderView(APIView):
    # the user be logged in
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # check if the cart is empty
        cart = Cart.objects.get(user=request.user)
        if not cart or cart.items.count() == 0:
            return Response({"error": "Cart is empty"})
        
        # create the order
        order = Order.objects.create(
            user = request.user,
            subtotal = cart.subtotal,
            tax_amount = cart.tax_amount,
            grand_total = cart.grand_total
        )
        
        # create order items
        
        # clear the cart items
        
        # send the notification email
        
        # send the response to frontend