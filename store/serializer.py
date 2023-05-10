from rest_framework import serializers
from decimal import Decimal
from store.models import Product,Collection

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)




class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length =255)
    price =serializers.DecimalField(max_digits=6,decimal_places=2,source ='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculatax')
    collection = serializers.HyperlinkedRelatedField(
        queryset = Collection.objects.all(),
        view_name= 'collection-detail'
    )
    
    def calculatax(self,product):
        
        return product.unit_price * Decimal(1.1)