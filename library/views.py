from django.shortcuts import render, redirect
from django.db.models import Q 
from .models import Book, Borrowed_book, Reminder, Wishlist
from django.contrib.auth.decorators import login_required
from django.utils import timezone

import datetime


# Create your views here.

def book_catalog(request):
    books = Book.objects.all()
    return render(request, 'library/book_catalog.html', {'books': books})



def book_search(request):
    if request.method == 'POST':
        query = request.POST['query']
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        return render(request, 'library/book_catalog.html', {'books': books})
    else:
        return render(request, 'library/book_catalog.html')

def book_reservation(request, book_id):
    book = Book.objects.get(id=book_id)
    book.availability = False
    book.save()
    return render(request, 'library/book_detail.html', {'book': book})


def borrow_book(user, book):
    if book.is_avilable:
        borrowed_book = Borrowed_book(user=user, book=book, due_date=datetime.date.today() + datetime.timedelta(days=14))
        borrowed_book.save()
        book.is_available = False
        book.save()
        return redirect('book_detail', book=book)
    else:
        return False

def return_book(borrowed_book):
    borrowed_book.returned_date = datetime.date.today()
    borrowed_book.save()
    book = borrowed_book.book
    book.is_available = True
    book.save()
    return redirect('book_detail', book=book)

def send_reminder(borrowed_book):
    reminder_date = borrowed_book.due_date - datetime.timedelta(days=3)
    reminder = Reminder(user=borrow_book.user, book=borrow_book.book, reminder_date = reminder_date)
    reminder.save()

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_detail.html', {'book': book})


def add_to_wishlist(request, book_id):
    book = Book.objects.get(id=book_id)
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    book = Book.objects.get(pk=book_id)
    user_wishlist.books.add(book)
    return redirect('book_detail', book=book)