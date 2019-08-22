from rest_framework import serializers

from shop_car.models import Cart


class CartSerializer(serializers.ModelSerializer):


    class Meta:
        model = Cart
        fields = '__all__'