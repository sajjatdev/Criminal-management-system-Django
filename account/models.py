
from settings.models import District, Postion, Station
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
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


class Account(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False,)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ForeignKey(
        'auth.Group',
        related_name='group',
        blank=True,
        null=True,
        verbose_name='User Roles',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Account List'

    def Name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name


class StaffAccountProfile(models.Model):
    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name="StaffAccount")

    image = models.ImageField(upload_to="profile/",
                              verbose_name="Photo", default="profile/photo.jpeg")

    cardNumber = models.CharField(
        max_length=255, unique=True, verbose_name="ID Number",)
    cardImage = models.ImageField(
        upload_to="cardImage/", verbose_name="ID Photo",  default="cardImage/card.jpeg")
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    position = models.ForeignKey(Postion, on_delete=models.CASCADE)

    class Meta:
        db_table = "staffProfile"
        verbose_name = 'Staff Profile  List'
        verbose_name_plural = 'Staff Profile  List'

    def __str__(self):
        return self.cardNumber


class UserAccount(models.Model):
    userAccount = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name="UserAccount")
    image = models.ImageField(upload_to="profile/",
                              verbose_name="Photo", blank=True, default="profile/photo.jpeg")

    station = models.CharField(max_length=255, default=0, blank=True)
    address = models.CharField(
        max_length=255, verbose_name="Address", blank=True)

    class Meta:

        verbose_name = 'User Account'
        verbose_name_plural = 'User Accounts List'

    def __str__(self):
        return self.userAccount
