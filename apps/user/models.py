# apps/users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    TAG_CHOICES = (
        ('green', 'Green'),
        ('yellow', 'Yellow'),
    )

    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default='user'
    )
    badge_type = models.CharField(
        max_length=10, choices=TAG_CHOICES, default='green'
    )

    referrer = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='referrals'
    )
    referral_code = models.CharField(
        max_length=10, unique=True, blank=True
    )

    wallet_balance = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00
    )

    phone_number = models.CharField(
        max_length=15, blank=True, null=True
    )

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
