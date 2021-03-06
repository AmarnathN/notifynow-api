from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# from phone_field import PhoneField
from django.contrib.postgres.fields import JSONField
from django.conf import settings

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
    phone_number = models.CharField(max_length=15)
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


class UserMail(models.Model):
    """ The mails received for the user """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    mail_from = models.EmailField(max_length=255, blank=True, null= True)
    user_mail = JSONField()

    def __str__(self):
        return self.user.email + ' - ' + str(self.mail_from)


class NetflixProfile(models.Model):
    """ The Netflix Profiles of the user """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    profile = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    last_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "profile"]
        ordering = ["user"]

    def __str__(self):
        return self.user.email + " - " + self.profile


class Notification(models.Model):
    """ The Notification type for Notify """

    notification_type = models.CharField(max_length=255)

    class Meta:
        ordering = ["notification_type"]

    def __str__(self):
        return self.notification_type

class Consent(models.Model):
    """ The User consents for Notify """

    # need to update as on-to-one field
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notification_type = models.ForeignKey(Notification, default=1, related_name='type', on_delete=models.CASCADE )
    whatsapp = models.BooleanField(default=True)
    chrome_ext = models.BooleanField(default=True)

    class Meta:
        unique_together = ["user", "notification_type"]
        ordering = ["user"]

    def __str__(self):
        return self.user.email + " - " + self.notification_type.notification_type


class ForwardMailId(models.Model):
    """ The User consents for Notify """

    # need to update as on-to-one field
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True
    )
    gmail_fwd_mail = models.EmailField(max_length=255)

    class Meta:
        unique_together = ["user", "gmail_fwd_mail"]
        ordering = ["user"]

    def __str__(self):
        return self.user.email

