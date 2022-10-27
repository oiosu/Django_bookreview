from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # add additional fields in here

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"

