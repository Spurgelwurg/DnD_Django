from django.db import models
from django.contrib.auth.models import AbstractUser

class DnDUser(AbstractUser):
    ROLE_CHOICES = (
        ('player', 'Player'),
        ('gamemaster', 'Game Master'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='player')

