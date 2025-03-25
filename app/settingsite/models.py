from django.db import models
from books.models import TimeMixin

# Create your models here.

class Manzil(TimeMixin):
    joylashov = models.CharField(max_length=50, blank=True)
    tel_number = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)


class BizHaqimizda(TimeMixin):
    body = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.body is None:
            self.body=="Books apps"
        super().save(*args, **kwargs)

