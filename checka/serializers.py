from rest_framework import serializers
from . models import PaymentCheck, Shop
from django.contrib.auth.models import User

class CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentCheck
        fields = ('date_added', 'shop', 'total_amount', 'photo' )


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = ('date_added', 'name', 'type')

