from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime
from django.db import models
#from django.contrib.auth.models import User

from django.core.validators import MinValueValidator
from django.db import models

from time import time


class Product(models.Model):
    CHOICE=(
        ('Grocery','Grocery'),
        ('Mobiles','Mobiles'),
        ('Clothes','Clothes'),
        ('Electronics','Electronics'),
        ('Home Appliances','Home appliances'),
        ('Beauty','Beauty'),
        ('Toys','Toys'),
        ('Sports','Sports'),
        ('Footwear','Footwear'),
        ('Others','Others')
    )
    option=(
        ('Sell','Sell'),
        ('Rent','Rent')

    )
#    seller_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name='%(class)s_seller')
    name = models.CharField(max_length=50, blank=False,unique=True)
    desp = models.TextField(max_length=500, blank=False, null=True)
    category = models.CharField(max_length=50, blank=True,null=True,choices=CHOICE)
    minimum_price = models.IntegerField(blank=True, validators=[MinValueValidator(1)],default=1)
    start = models.DateTimeField(default=timezone.now, null=True)
    end = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=10))
    current_bid = models.IntegerField(default=0)
    product_sold = models.BooleanField(default=False)
    choose = models.CharField(max_length=50, blank=True,null=True,choices=option)
   # bidder_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_bidder')
    rent_status = models.BooleanField(default=False)
   # rent_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_rent')
    rent_price = models.IntegerField(default=0)
    rent_time_start = models.DateTimeField(null=True)
    rent_time_end = models.DateTimeField(null=True)
    rent_fine = models.IntegerField(default=0)
    # bid_only = models.BooleanField(default=False)
    # rent_only = models.BooleanField(default=False)
    # rent_and_bid = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)
