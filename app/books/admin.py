from django.contrib import admin
from .models import Book, Like, Download

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "likes_count", "downloads_count", "daraja", "created_at")
    search_fields = ("title", "author")

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "created_at")
    search_fields = ("user__username", "book__title")

@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "created_at")
    search_fields = ("user__username", "book__title")