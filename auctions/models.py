from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    starting_bid = models.IntegerField()
    category = models.CharField(max_length=255)
    #image of object url = ...do we need a field for this?
    winner = models.ForeignKey(User, related_name='Auction_Winner', on_delete=models.CASCADE)
    #created = models.DateTimeField(editable=False, null=True)
    #expires = models.DateTimeField(editable=False, null=True)

class Bids(models.Model):
    auction = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='bid_owner', on_delete=models.CASCADE)
    bid_amount = models.IntegerField()


class Comments(models.Model):
    post = models.CharField(max_length=255)
    author = models.CharField(max_length=200)
    text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
