from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    startingBid = models.IntegerField()
    image = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}: {self.startingBid}"
