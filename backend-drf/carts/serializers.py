from rest_framework import serializers
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    price = serializers.DecimalField(source="product.price", max_digits=10, decimal_places=2, read_only=True)
    tax_percent = serializers.DecimalField(source="product.tax_percent", max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = CartItem
        fields = "__all__"
        
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    subtotal = serializers.SerializerMethodField() #this gonna bring the get_subtotal() method
    total = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = "__all__"
        
    def get_subtotal(self, obj): # here obj means Cart model instance
        subtotal = 0
        for item in obj.items.all(): # here items is the related name of cart from CartItem class in models
            subtotal = subtotal + item.product.price * item.quantity
        return subtotal
    
    def get_total(self, obj):
        total = 0
        for item in obj.items.all():
            subtotal = item.product.price * item.quantity
            tax = subtotal * (item.product.tax_percent/100)
            total += subtotal + tax
        return total