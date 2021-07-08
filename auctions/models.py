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
    active = models.BooleanField()
    

    def __str__(self):
        return f"{self.title}: {self.startingBid}"
