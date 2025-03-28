from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    newsletter_abo = models.BooleanField(default=False)
    email_address = models.EmailField(default="")
    account = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Bill(models.Model):
    total_amount = models.FloatField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.order.pk} | {self.total_amount} €"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="Producttype")
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk}"


class Producttype(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type_name}"
