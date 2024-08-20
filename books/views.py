from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView
# Create your views here.

class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "book/book_list.html"
    
class BookDetailView(DetailView): # new
    model = Book
    template_name = "books/book_detail.html"
