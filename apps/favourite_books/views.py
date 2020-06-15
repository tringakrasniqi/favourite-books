from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book
from apps.authenticate.models import User

def feed(request):
      if 'uid' in request.session:
            context = {
                  'all_books': Book.objects.all(),
                  'logged_user': User.objects.get(id=request.session['uid'])
            }
            return render(request, 'feed.html', context)
      else:
            return redirect('/')

def add_book(request):
      errors = Book.objects.basic_validator(request.POST)

      if len(errors) > 0:
            for key, value in errors.items():
                  messages.error(request, value)
            return redirect('/')
      else:
            creator = User.objects.get(id=request.session['uid'])
            book = Book.objects.create(title=request.POST['title'], desc=request.POST['description'], uploaded_by=creator)
            book.users_who_favourite.add(creator)
            return redirect('/')

def show_one(request, book_id):
      book = Book.objects.get(id=book_id)
      edit_mode = False
      if book.uploaded_by.id == request.session['uid']:
            edit_mode = True
      context = {
            'book_details' : book,
            'edit_mode' : edit_mode,
            'logged_user': User.objects.get(id=request.session['uid'])
      }
      return render(request, 'show_book.html', context)

def edit_book(request, book_id):
      book = Book.objects.get(id=book_id)
      book.title = request.POST['title']
      book.desc = request.POST['description']
      book.save()
      return redirect(f"/books/show_one/{book.id}")

def delete_book(request, book_id):
      Book.objects.get(id=book_id).delete()
      return redirect('/books')

def toggle_favourite(request, book_id):
      book = Book.objects.get(id=book_id)
      logged_user = User.objects.get(id=request.session['uid'])
      if book in logged_user.favourited_books.all():
            logged_user.favourited_books.remove(book)
      else:
            logged_user.favourited_books.add(book)
      return redirect('/books')