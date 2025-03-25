from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class TimeMixin(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Book(TimeMixin):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150, blank=True, null=True)
    body = models.TextField()
    malumot = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to="images/")
    pdf = models.FileField(upload_to="pdf/")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    downloads_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    daraja = models.PositiveIntegerField(default=0)
    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"

    def __str__(self):
        return self.title
    
class Like(TimeMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_books")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        unique_together = ('user', 'book')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.book.likes_count = self.book.likes.count()
        self.book.save()

class Download(TimeMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="downloaded_books")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="downloads")

    class Meta:
        verbose_name = "Yuklab olish"
        verbose_name_plural = "Yuklab olishlar"
        unique_together = ('user', 'book')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.book.downloads_count = self.book.downloads.count()
        self.book.save()

# class SettingsSite(TimeMixin):
