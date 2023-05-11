from rest_framework import serializers
from decimal import Decimal
from store.models import Product,Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields =[ 'id','title','products_count']
    
    products_count = serializers.IntegerField(read_only =True)
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length = 255)




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','unit_price','description','slug','inventory','price_with_tax','collection']
    price_with_tax = serializers.SerializerMethodField(method_name='calculatax')
    
    
    def calculatax(self, product):
        if isinstance(product, dict):
            unit_price = product.get('unit_price')
        else:
            
            unit_price = product.unit_price
        
        return unit_price * Decimal(1.1)

# def calculatax(self,product:Product):
        
#         return product.unit_price * Decimal(1.1)