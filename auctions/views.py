from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from .models import User, Listing, Comment

# Not in use; need to know how to apply Bootstrap styles to auto-generated forms.
class NewListingForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="description")
    image = forms.CharField(label="Image URL")
    startingBid = forms.IntegerField(label="Starting Bid")

class NewCommentForm(forms.Form):
    content = forms.CharField(label="Comment")



def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
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
def newListing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        startingBid = request.POST["startingBid"]
        image = request.POST["image"]
        currentUser = request.user
        user = User.objects.get(pk=currentUser.id)
        newListing = Listing.objects.create(title=title, description=description, startingBid=startingBid, image=image, user=user)

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/newListing.html", {
            "form": NewListingForm()
        })

def listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "comments": Comment.objects.filter(listing=listing),
        "commentForm": NewCommentForm()
    }) 

# TODO: Toggle listing when watch button is pressed again
def wishlist(request,listing_id):
    if request.method == "POST":
        currentUser = request.user
        user = User.objects.get(pk=currentUser.id)
        listing = Listing.objects.get(pk=listing_id)
        user.wishlist.add(listing)
    return HttpResponseRedirect(reverse("index"))

def comment(request, listing_id):
    if request.method == "POST":
        theUser = request.user
        currentUser = User.objects.get(pk=theUser.id)
        currentListing = Listing.objects.get(pk=listing_id)
        newComment = Comment(content=request.POST["content"], listing=currentListing,user=currentUser)
        newComment.save()
    return HttpResponseRedirect(reverse("listing", args=(listing_id,)))

def toggleAuction(request, listing_id):
    if request.method == "POST":
        theUser = request.user
        currentUser = User.objects.get(pk=theUser.id)
        currentListing = Listing.objects.get(pk=listing_id)
        print(currentListing.active)
        if currentListing.user == currentUser:
            currentListing.active = not currentListing.active
            currentListing.save()
            print(currentListing.active)
    return HttpResponseRedirect(reverse("listing", args=(listing_id,)))

