"""
Module: models.py
Description: This module contains the User model and UserManager for managing user creation in a Django project.

Classes:
    UserManager: A custom user manager class responsible for creating and managing users.
    User: A custom user model extending the AbstractUser class provided by Django.

Usage:
    This module defines a custom user model and user manager. To use them, include this module in your Django project
     and configure the settings to use the custom user model.

Example:
    # In settings.py
    AUTH_USER_MODEL = 'your_app.User'

    # In a view or elsewhere
    from your_app.models import User
    user = User.objects.create_user(username='example_user', password='password123')
"""
import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class UserManager(BaseUserManager):
    """
    Custom manager for the User model.
    """

    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a regular user with the given username and password.

        Args:
            username (str): The username for the user (in this case, phone number).
            password (str): The password for the user.
            extra_fields (dict): Additional fields to be saved with the user.

        Returns:
            User: The created user instance.
        """
        if not username:
            raise ValueError('Users must have a phone number!')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given username and password.

        Args:
            username (str): The username for the superuser (in this case, phone number).
            password (str): The password for the superuser.
            extra_fields (dict): Additional fields to be saved with the superuser.

        Returns:
            User: The created superuser instance.
        """
        user = self.create_user(username, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """
    Custom user model extending the AbstractUser class provided by Django.
    """

    username = models.CharField(max_length=155, unique=True)
    email = models.EmailField(unique=False, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()


# -----------------------------------------------------------------------------------------------------


# Create a RegexValidator instance with the numeric pattern
validation_telegram_id = RegexValidator(
    regex=r'^[0-9]+$',
    message='Telegram ID must contain only numbers.',
)


class Client(models.Model):
    """
    Represents a client in the cargo system.

    Attributes:
        fullname (str): The full name of the client.
        telegram_id (str): The Telegram ID of the client.
        keyword (str): The auto-generated keyword for the client.
        given_time (datetime): The date and time when the client was added to the system.
    """

    fullname = models.CharField(max_length=100, help_text="The full name of the client.")
    telegram_id = models.CharField(
        max_length=50,
        unique=True,
        help_text="The Telegram ID of the client.",
        validators=[validation_telegram_id],  # Apply the validator
    )
    keyword = models.CharField(max_length=50, unique=True, help_text="The auto-generated keyword for the client.",
                               null=True, blank=True)
    given_time = models.DateField(auto_now_add=True,
                                  help_text="The date and time when the client was added to the system.")

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to generate the keyword for the client.
        """
        if not self.pk:
            last_client = Client.objects.last()
            if last_client:
                last_keyword = last_client.keyword
                last_number = int(last_keyword[3:])
                new_number = last_number + 1
                self.keyword = f'AAA{new_number}'
            else:
                self.keyword = 'AAA1'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        """
        Returns the full name of the client.
        """
        return self.fullname


# -----------------------------------------------------------------------------------------------------


class Party(models.Model):
    """
    Model representing a party.
    """

    title = models.CharField(max_length=100, help_text="The title of the party.")
    """
    The title of the party.
    
    Examples:
        "Birthday Bash"
    """

    created_at = models.DateField(help_text="The date and time when the party was created.")
    """
    The date and time when the party was created.

    Examples:
        "2024-04-08"
    """

    def __str__(self):
        return self.title


# -----------------------------------------------------------------------------------------------------


class ChineseStorage(models.Model):
    """
    Model representing Chinese storage of products.
    """

    trek_code = models.UUIDField(default=uuid.uuid4, help_text="The Trek code of the product.", max_length=16)
    """
    The Trek code of the product.
    Examples:
        "550e8400-e29b-41d4-a716-446655440000"
    """

    product_title = models.CharField(max_length=100, help_text="The title of the product.")
    """
    The title of the product.
    Examples:
        "Chinese Teapot"
    """

    product_count = models.PositiveIntegerField(help_text="The quantity of the product.")
    """
    The quantity of the product.
    Examples:
        10
    """

    product_weight = models.FloatField(help_text="The weight of the product.")
    """
    The weight of the product.
    Examples:
        2.5
    """

    box = models.CharField(max_length=100, help_text="The box of the product.")
    """
    The box of the product.
    Examples:
        "Box A"
    """

    client_keyword = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='chinese_storages',
                                       help_text="The keyword of the client.")
    """
    The keyword of the client.
    Examples:
        Client object (1)
    """

    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='chinese_storages',
                              help_text="The title of the party.")
    """
    The title of the party.
    Examples:
        Party object (1)
    """

    created_at = models.DateField(help_text="The date and time when the product was created.")
    """
    The date and time when the product was created.
    Examples:
        "2024-04-08"
    """

    def __str__(self):
        return self.product_title


# -----------------------------------------------------------------------------------------------------

class UzbekStorage(models.Model):
    """
    Model representing Uzbek storage of products.

    Attributes:
        client (ForeignKey): The client associated with the UzbekStorage.
        chinese_storage (ForeignKey): The ChineseStorage associated with the UzbekStorage.
        party (ForeignKey): The party associated with the UzbekStorage.
        created_at (DateField): The date and time when the UzbekStorage was created.
        price (DecimalField): The price of the product stored in UzbekStorage.
        status (BooleanField): The status indicating whether the product is available or not.
    """

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='uzbek_storages',
                               help_text="The keyword of the client.")
    chinese_storage = models.ForeignKey(ChineseStorage, on_delete=models.CASCADE, related_name='uzbek_storages',
                                        help_text="The Trek code of the product.")
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='uzbek_storages',
                              help_text="The title of the party.")
    created_at = models.DateField(help_text="The date and time when the product was created.")
    price = models.FloatField(help_text="The price of the product.")
    status = models.BooleanField(default=False, help_text="The status of the product.")

    def __str__(self):
        return self.chinese_storage.product_title
