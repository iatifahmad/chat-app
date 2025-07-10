from django.db import models                       
from django.contrib.auth.models import AbstractUser,BaseUserManager

from django.db import models
# from users.models import User


class UserManager(BaseUserManager):
    
    def create_user(self, email, first_name, last_name,number,password=None, is_staff = False, is_superuser = False, **extra_fields):
        if not email:
            raise ValueError("u must have an email")
        if not first_name:
             raise ValueError("u must have an first name")
        if not last_name:
             raise ValueError("u must have an last name")
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        if number is not None:
            user.number = number
        user.set_password(password)
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user
    def create_superuser(self,email, first_name, last_name,password=None):
        user = self.create_user( email = email, first_name = first_name, last_name = last_name,password=password, is_staff=True, is_superuser=True)
        user.save()
        return user
            
class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True) 
    password =models.CharField(max_length=100)
    number = models.IntegerField(blank=True, null=True)  # <-- new field added
    username = None
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [ "first_name", "last_name"]
    
    


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.sender} to {self.receiver}: {self.content[:20]}"