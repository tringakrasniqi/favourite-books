from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
      def register_validator(self, post_data):
            errors = {}
            user = User.objects.filter(email = post_data['email'])
            if user: 
                  errors['email'] = "An account with this email already exists"
                  return errors
            if len(post_data['first_name']) < 2:
                  errors['first_name'] = "First name cannot be less than 2 characters"
            if len(post_data['last_name']) < 2:
                  errors['last_name'] = "Last name cannot be less than 2 characters "
            if not EMAIL_REGEX.match(post_data['email']):
                  errors['email'] = "Invalid email address!"
            if len(post_data['password']) < 8:
                  errors['password'] = "Password cannot be less than 8 characters"
            elif post_data['password'] != post_data["confirm_password"]:
                  errors['confirm_password'] = "Passwords do not match"
            return errors
      def login_validator(self, post_data):
            errors = {}
            user = User.objects.filter(email = post_data['email'])
            if user:
                  logged_user = user[0]
                  if not bcrypt.checkpw(post_data['password'].encode(), logged_user.password.encode()):
                        errors['email'] = "Email and password do not match"
            else :
                  errors['email'] = "This email is not registered yet" 
            return errors

class User(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      password = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      objects = UserManager()