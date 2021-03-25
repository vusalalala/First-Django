from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=150)
    message = models.TextField(blank=True)


def __str__(self):
    return self.email


# Create your models here.
