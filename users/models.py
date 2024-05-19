from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# Create your models here.
class User(AbstractUser):
    CUSTOMER = 'customer'
    SELLER = 'seller'
    INVESTER = 'invester'
    ROLE_CHOICES = [
    (CUSTOMER, 'Customer'),
    (SELLER, 'Seller'),
    (INVESTER, 'Invester'),
    ]


    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    USERNAME_FIELD = 'email'
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CUSTOMER,)
    file = models.FileField(upload_to='uploads/documents/',null=True)
    REQUIRED_FIELDS = []
    is_verified = models.BooleanField(default=False)
    img = models.FileField(upload_to='uploads/profile/',null=False)


    objects = CustomUserManager()

    def __str__(self) :
        return self.email