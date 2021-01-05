from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required
import operator


from .models import User,Listing,Bids, Comments

auction_list = []



def index(request):
    listings = Listing.objects.exclude(active=False).all()
    return render(request, "auctions/index.html", {
        "listings": listings,
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):

    if request.method == "POST":
        listing = Listing()
        listing.seller = request.user
        listing.title = request.POST["title"]
        listing.descrip = request.POST["descrip"]
        listing.start_bid = request.POST["start_bid"]
        listing.category = request.POST["category"]
        listing.image = request.POST["image"]
        listing.date = datetime.today().strftime('%Y-%m-%d %H:%M')
        listing.active = True
        listing.save()

        return render(request, "auctions/listing.html", {
            "listing" : listing,
            })
    else:
        return render(request, "auctions/create.html", {
        "listing": Listing()
        })


def listing(request, listing_id):

    listing = Listing.objects.get(id=listing_id)
    list_faves = listing.favourited.all()
    ordered_comments = listing.comments.all().order_by('-created_on')
    message = None
    new_comment = None
    categories = ['clothing','electronics']

    if request.method == "POST":
        if 'bid' in request.POST:
            if float(request.POST["bid"]) > listing.start_bid:
                bid = Bids()
                bid.user = request.user
                bid.listing = listing
                bid.date = datetime.today().strftime('%Y-%m-%d %H:%M')
                bid.save()

                listing.start_bid =  request.POST["bid"]
                listing.last_bid = bid.date
                listing.winner = bid.user
                listing.save()
            else:
                message = "ERROR: Your bid must be greater than the current bid to be valid!"

        elif 'faved' in request.POST:
            list_faves = listing.favourited.all()
            if request.user in list_faves:
                listing.favourited.remove(request.user)
            else:
                listing.favourited.add(request.user)

        elif 'terminate' in request.POST:
            listing.active = False
            listing.favourited.remove(request.user)
            listing.save()

        elif 'comment' in request.POST:
            comment = Comments()
            comment.listing = listing
            comment.text = request.POST["comment"]
            comment.author = request.user
            comment.created_on = datetime.today().strftime('%Y-%m-%d %H:%M')
            comment.save()



    return render(request, "auctions/listing.html", {
        "listing": listing,
        "message": message,
        "comments": ordered_comments,
        "categories": categories
        })


@login_required
def watchlist(request,user_id):
    user = User.objects.get(id = user_id)
    wl = user.faves.all()
    return render(request, "auctions/watchlist.html", {
        "user": user,
        "wl": wl
    })

def category(request, category_id):
    listing = Listing.objects.all()
    category = listing.filter(category= category_id).all()
    return render(request, "auctions/category.html", {
        "category": category,
        "cat_type": category_id,

    })
