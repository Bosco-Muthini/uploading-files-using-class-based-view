from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from .forms import BookForm
from .models import Book
# Create your views here.
class BookListView(ListView):
    model=Book
    template_name='class_book_list.html'
    

class UploadBookView(CreateView):
    model=Book
    fields=('title','author','pdf','cover')
    success_url=reverse_lazy('class_book_list')
    template_name='class_upload_book.html'