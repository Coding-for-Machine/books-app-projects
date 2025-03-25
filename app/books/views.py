from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, FileResponse
from django.contrib.auth.decorators import login_required
from .models import Book, Like, Download

def book_list(request):
    books_popular = Book.objects.filter(is_active=True).order_by("-created_at")
    books = Book.objects.filter(is_active=True).order_by("-created_at")
    nev_books = Book.objects.filter(is_active=True).order_by("-created_at")
    return render(request, "index.html", {"books": books, "books_popular": books_popular, "nev_books": nev_books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id, is_active=True)
    is_liked = request.user.is_authenticated and Like.objects.filter(user=request.user, book=book).exists()
    return render(request, "books/book_detail_.html", {"book": book, "is_liked": is_liked})

@login_required
def download_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, is_active=True)
    download, created = Download.objects.get_or_create(user=request.user, book=book)
    
    if created:
        book.downloads_count += 1
        book.save()
    if download or created:
        book.daraja += 1
        book.save()

    return FileResponse(book.pdf.open(), as_attachment=True, filename=f"{book.title}.pdf")

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class ToggleLikeView(View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id, is_active=True)
        like, created = Like.objects.get_or_create(user=request.user, book=book)

        if not created:
            like.delete()
            book.likes_count -= 1
            book.daraja -= 1
            liked = False
        else:
            book.likes_count += 1
            book.daraja += 1
            liked = True

        book.save()
        return JsonResponse({"liked": liked, "likes_count": book.likes_count})

