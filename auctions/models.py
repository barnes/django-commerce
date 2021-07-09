from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    wishlist = models.ManyToManyField(
        'Listing',
        blank=True,
        related_name="list_item"
    )

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    startingBid = models.IntegerField()
    image = models.CharField(max_length=64)
    active = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.title}: {self.startingBid}"

class Comment(models.Model):
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user" )
    content = models.CharField()

