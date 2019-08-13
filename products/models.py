from django.db import models
from django.utils import timezone


class Universal(models.Model):
    brand_name = models.CharField(max_length=100)
    model = models.CharField(max_length=255)
    product_img = models.CharField(max_length=255, default='')
    processor = models.CharField(max_length=255)
    ram = models.CharField(max_length=50, default=0)
    storage = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    description = models.TextField(default='')
    price = models.CharField(max_length=255, default='0')
    number_in_stock = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Phone(Universal):
    ph_id = models.CharField(max_length=5, default='170')
    battery = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)

    def __str__(self):
        return self.model

    class Meta():
        ordering = ('date_added',)
        get_latest_by = ('date_added',)


class Laptop(Universal):
    lap_id = models.CharField(max_length=5, default='180')
    GPU = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="")
    ports = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.model


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()


    def __str__(self):
        return self.name
    