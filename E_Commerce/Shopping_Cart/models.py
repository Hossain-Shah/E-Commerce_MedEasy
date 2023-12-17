#importing libraries
from django.db import models

#Customer table building
class Customer(models.Model):
    id = models.BigAutoField(
                                primary_key=True, 
                                editable=False,
                                unique=True
                            )                          
    name = models.CharField(max_length=100)
    review = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = "Shopping_Cart"

#Product table building
class Product(models.Model):
    id = models.BigAutoField(
                                primary_key=True, 
                                editable=False,
                                unique=True
                            )
    ordered_image = models.ImageField(upload_to="ordered_images/")
    delivered_image = models.ImageField(upload_to="delivered_images/")
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.FloatField()
    availability = models.BooleanField(default=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        app_label = "Shopping_Cart"