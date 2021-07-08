from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ("id","title", "description", "startingBid", "image")



# Register your models here.
admin.site.register(Listing, ListingAdmin)