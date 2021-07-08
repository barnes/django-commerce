from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Listing, User

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id","title", "description", "startingBid", "image", "active")

class UsersAdmin(admin.ModelAdmin):
    filter_horizontal = ("wishlist",)



# Register your models here.
admin.site.register(Listing, ListingAdmin)
admin.site.register(User, UsersAdmin)