from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(default="")
    newsletter = models.BooleanField(default=False)
    account_balance = models.FloatField(blank=True, null=True)
