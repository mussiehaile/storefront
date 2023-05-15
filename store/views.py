from django.shortcuts import render,get_object_or_404
from django.db.models.aggregates import Count
from django.http import HttpResponse
from store.filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework import status
from .models import Product,Collection,Review,Cart
from .serializer import ProductSerializer,CollectionSerializer,ReviewSerializer,CartSerializer,CartItemSerializer,AddCartItemSerializer,UpdateCartItemSerializer
from store.models import OrderItem,CartItem
from .pagination import DefaultPagination


# Create your views here.



class ProductViewSet(ModelViewSet):
    serializer_class =ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['title','description']
    ordering_fields = ['unit_price','last_update']
    
    def get_serializer_context(self):
        return {'request':self.request}


    def delete(self,request,pk):
        product = get_object_or_404(Product,pk =pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    




class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    
    
    
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id =kwargs['PK']).count() >0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    
    
    
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk'])
    
    
    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}
    


class CartViewSet(CreateModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    queryset =Cart.objects.prefetch_related('items__product').all()
    serializer_class= CartSerializer
    
   
    

class CartItemViewset(ModelViewSet):
    
    http_method_names = ['get','post','patch','delete']
    
    def get_serializer_class(self):
        if self.request.method =='POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_id':self.kwargs['cart_pk']}
    
    def get_queryset(self):
        return CartItem.objects.\
    filter(cart_id = self.kwargs['cart_pk']).\
     select_related('product')
    

















# @api_view(['GET', 'PUT', 'DELETE'])
# def collection_detail(request, pk):
#     collection = get_object_or_404(
#         Collection.objects.annotate(
#             products_count=Count('products')), pk=pk)
    # if request.method == 'GET':
    #     serializer = CollectionSerializer(collection)
    #     return Response(serializer.data)
    # elif request.method == 'PUT':
    #     serializer = CollectionSerializer(collection, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    # elif request.method == 'DELETE':
    #     if collection.products.count() > 0:
    #         return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    

# @api_view(['GET', 'POST'])
# def collection_list(request):
#     if request.method == 'GET':
#         queryset = Collection.objects.annotate(products_count=Count('products')).all()
#         serializer = CollectionSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    

    