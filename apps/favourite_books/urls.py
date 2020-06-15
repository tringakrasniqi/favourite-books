from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed),
    path('add', views.add_book),
    path('show_one/<int:book_id>', views.show_one),
    path('<int:book_id>/edit', views.edit_book),
    path('<int:book_id>/delete', views.delete_book),
    path('<int:book_id>/favourite', views.toggle_favourite)
]












