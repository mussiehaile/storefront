from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count,Min
from django.db.models import Value
from django.db.models import Q , F,Func,ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models import DecimalField
from django.contrib.contenttypes.models import ContentType
from store.models import Product ,OrderItem,Order,Customer
from tags.models import TaggedItem



def say_hello(request):
    #aggregation 
    #result = Product.objects.aggregate(count = Count('id'),min_price= Min('unit_price'))
    
    #query_set = Product.objects.filter(unit_price__range =(20,40))    #if we are using get we get object not query set
    #product= Product.objects.get(pk =1)
    #exists = Product.objects.filter(pk =0).exists()
    # for products in query_set:
    #     print(query_set)
       #using list on query set since it is lazy 
    # list(query_set)
    
    # filtering if some string is ina tilte column or not 
    #query_set = Product.objects.filter(title__icontains ='coffee')
    
    # what if i wan use dates as filtering criteria
    #query_set =Product.objects.filter(last_update__year = 2021)
    
    # what if i wan find items with null
    #query_set = Product.objects.filter(description__isnull =True)
    
    # what we wan coct using and operation
    #query_set = Product.objects.filter(inventory__lt =10).filter(unit_price__lt =20)
    
    #what if we wan perform or operation using q
    #query_set =Product.objects.filter( Q (inventory__lt =13) | Q ~(unit_price__lt =17) )
    
    #what if we wan compare between 2 filds
    #query_set = Product.objects.filter(inventory = F('unit_price'))
    
     # sorting order by returns query set
    #query_set = Product.objects.order_by('unit_price','-title')
    # #earliest returns objects
    
    # pro = Product.objects.earliest('unit_price')
    # pro2 = Product.objects.latest('unit_price')
    
    #limiting results
    #query_set = Product.objects.all()[:5]
    
    #selecting columns just like select in sql
    #query_set = Product.objects.values_list('id','title', 'collection__title')
    
    #selecting from product which user is selected from the other table
    #query_set =Product.objects.filter(id__in =OrderItem.objects.values('product__id').distinct()).order_by('title')
    
    # same as values 
    #query_set = Product.objects.only('id','title')
    
    #hold some columns which is not needed right away in this case hold description.
    #query_set = Product.objects.defer('description').all()
    
    #selecting from both tables using select_related  and we use select related when thair is one to one relation
    #query_set = Product.objects.select_related('collection').all()
    
    # use prefech related if thair is a one to many and many to many relationship between tables
    #query_set = Product.objects.prefetch_related('promotions').select_related('collection').all()
    
    #query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    
    #annotation
    #query_set = Product.objects.annotate(is_new =Value(True))
    
    #concatnation using func 
    # query_set = Customer.objects.annotate(
    #     full_name =Func(F('first_name') , Value(''), F('last_name'),function= 'CONCAT')
    # )
    
    #concatnation using concat class
    # query_set = Customer.objects.annotate(
    #     full_name =Concat(('first_name') , Value(''), ('last_name')))
    
    #creating new columns wthi each count of orders group by customer
    # query_set = Customer.objects.annotate(
    #     orders_count = Count('order')
    # )
    
    #expression wrapper
    # disco_price = ExpressionWrapper(F('unit_price') * 0.2, output_field= DecimalField())
    # query_set = Product.objects.annotate(
    #     disco_price =disco_price )
    
    contnttype = ContentType.objects.get_for_model(Product)
    taggeditem = TaggedItem.objects\
    .select_related('tag')\
        .filter(
        content_type = contnttype,
        object_id =1
    )
    
    return render(request, 'hello.html', {'name': 'Mosh','result':list(taggeditem)})
