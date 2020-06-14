from django.db import models
from apps.authenticate.models import User

class BookManager(models.Manager):
      def basic_validator(self, post_data):
            errors = {}
            if post_data['title'] == "" :
                  errors['title'] = "Title cannot be empty"
            if len(post_data['description']) < 5:
                  errors['description'] = "Description must be at least 5 characters"
            return errors

class Book(models.Model):
      title = models.CharField(max_length=255)
      desc = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      uploaded_by = models.ForeignKey(User,related_name="uploaded_books", on_delete=models.CASCADE)
      users_who_favourite = models.ManyToManyField(User, related_name="favourited_books")
      objects = BookManager()