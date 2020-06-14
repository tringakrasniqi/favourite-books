from django.urls import path, include

urlpatterns = [
    path('', include('apps.authenticate.urls')),
    path('books/', include('apps.favourite_books.urls'))
]
