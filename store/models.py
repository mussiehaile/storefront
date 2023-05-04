from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    
    
class Customer(models.Model):
    MEMBERSHIP_BRONZ = 'B'
    MEMBERSHIP_SILVER= 'S'
    MEMBERSHIP_GOLD = 'G'
    
    MEMBERSHIP_CHOISES =[
        (MEMBERSHIP_BRONZ,'bronz'),
        (MEMBERSHIP_SILVER,'silver'),
        (MEMBERSHIP_GOLD,'gold')
    ]
    first_name = models.CharField(max_length=255),
    last_name = models.CharField(max_length=255),
    email =models.EmailField(unique=True),
    phone = models.CharField(max_length=255),
    birth_date =  models.DateField(null=True)
    membership = models.CharField(max_length=255,choices=MEMBERSHIP_CHOISES,default=MEMBERSHIP_BRONZ)\
    
    
class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLITED = 'C'
    PAYMENT_FAILED = 'F'
    
    PAYMENT_CHICES = [
    (PAYMENT_PENDING ,'P'),
    (PAYMENT_COMPLITED ,'C'),
    (PAYMENT_FAILED ,'F'),
    ]
    
    placed_at = models.DateTimeField(auto_now=True)
    payment_status =models.CharField(max_length=255,choices=PAYMENT_CHICES,default=PAYMENT_PENDING)