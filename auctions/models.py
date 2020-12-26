from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):

    title = models.CharField(max_length=255)
    descrip = models.CharField(max_length=255, null=True)
    start_bid = models.DecimalField(max_digits=225, decimal_places=2, default = 0)
    category = models.CharField(max_length=255)
    image = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(editable=False, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #winner = models.ForeignKey(User, related_name='Auction_Winner', on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False, null=True)
    favourited = models.ManyToManyField(User, blank=True,default = None, related_name="faves")
    #manytomany - can access each way
    #(ie listing to users and users to listings)
    #the "related name" above means you dont have
    #to use user.listing_set.all() when doing
    #users to listings link (ie dont need _set)

class Bids(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
    #user = models.ForeignKey(User, related_name='bid_owner', on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=225, decimal_places=2)


class Comments(models.Model):
    post = models.CharField(max_length=255)
    author = models.CharField(max_length=200)
    text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
