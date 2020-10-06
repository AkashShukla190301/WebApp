from django.db import models

from django.urls import reverse

# Create your models here.


class Donar(models.Model):
    name=models.CharField(max_length=124);
    phone_number=models.PositiveIntegerField()
    email = models.EmailField()
    address=models.TextField(max_length=145)
    book_photo = models.ImageField(upload_to="book_photos", blank=True)

    def get_absolute_url(self):
        return reverse("index")