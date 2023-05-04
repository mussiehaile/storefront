from django.db import models

# Create your models here.


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null =True, related_name='+')
    
    
class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    unit_price =models.DecimalField(max_digits=6,decimal_places=2)
    order = models.ForeignKey('Order',on_delete=models.PROTECT)
    product = models.ForeignKey('Product',on_delete=models.PROTECT)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    

class CartItem(models.Model):
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)
    
    
    
    
class Customer(models.Model):
    MEMBERSHIP_BRONZ = 'B'
    MEMBERSHIP_SILVER= 'S'
    MEMBERSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOISES = [
        (MEMBERSHIP_BRONZ,'bronz'),
        (MEMBERSHIP_SILVER,'silver'),
        (MEMBERSHIP_GOLD,'gold')
    ]
    first_name = models.CharField(max_length=255),
    last_name = models.CharField(max_length=255),
    email =models.EmailField(unique=True),
    phone = models.CharField(max_length=255),
    birth_date =  models.DateField(null=True),
    membership = models.CharField(
                                  max_length=1,
                                  choices=MEMBERSHIP_CHOISES,
                                  default=MEMBERSHIP_BRONZ
                                  )
    
    
    
    
class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLITED = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_CHICES = [
    (PAYMENT_STATUS_PENDING ,'P'),
    (PAYMENT_STATUS_COMPLITED ,'C'),
    (PAYMENT_STATUS_FAILED ,'F'),
    ]
    
    placed_at = models.DateTimeField(auto_now=True)
    payment_status =models.CharField(max_length=1,
                                     choices=PAYMENT_CHICES,
                                     default = PAYMENT_STATUS_PENDING),
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    
    
    
# one_to_one relationship

class Address(models.Model):
    streat = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
    zip = models.CharField(max_length=10,null =True)

