from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from phone_field import PhoneField

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None, **extra_fields):
        """ Create and saves new user """
        if not email:
            raise ValueError("Users must have email Address")
        if not phone_number:
            raise ValueError("Users must have phone_number ")
        user = self.model(
            email=self.normalize_email(email), phone_number=phone_number, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)  # to support mutiple databases

        return user

    def create_superuser(self, email, phone_number, password):
        """ create and save super user """
        user = self.create_user(email, phone_number, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user models that supports email and phonenumber instead of database """

    email = models.EmailField(max_length=255, unique=True)
    phone_number = PhoneField(help_text="WhatsApp phone number")
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
