from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):

    title = models.CharField(max_length=255)
    descrip = models.CharField(max_length=255)
    start_bid = models.DecimalField(max_digits=225, decimal_places=2, default = 0)

    image = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(editable=False)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    last_bid = models.DateTimeField(editable=False,null=True)
    winner = models.ForeignKey(User, related_name='Auction_Winner',on_delete=models.CASCADE, null=True)
    favourited = models.ManyToManyField(User, blank=True,related_name="faves")
    active = models.BooleanField(default=True)
    category_CHOICE = [
    ('clothing','clothing'),
    ('food','food')
    ]
    category = models.CharField(max_length=225,
    choices=category_CHOICE,default= 'Other')

    #manytomany - can access each way
    #(ie listing to users and users to listings)
    #the "related name" above means you dont have
    #to use user.listing_set.all() when doing
    #users to listings link (ie dont need _set)

class Bids(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, related_name='bid_owner', on_delete=models.CASCADE)
    date = models.DateTimeField(editable=False)



class Comments(models.Model):
    listing = models.ForeignKey(Listing, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    created_on = models.DateTimeField(editable=False)
#    class Meta:
#        ordering = ['created_on']
#    def __str__(self):
#        return 'Comment {} by {}'.format(self.text, self.user)
