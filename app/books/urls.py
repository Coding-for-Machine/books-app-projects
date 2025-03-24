from django.urls import path
from .views import book_list, book_detail, download_book, ToggleLikeView

urlpatterns = [
    path("", book_list, name="book_list"),
    path("<int:book_id>/", book_detail, name="book_detail"),
    path("<int:book_id>/download/", download_book, name="download_book"),
    path("<int:book_id>/like/", ToggleLikeView.as_view(), name="toggle_like"),
]
