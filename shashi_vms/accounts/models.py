from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.utils.functional import cached_property
from django.db.models import Q

STATUS_CHOICES = (
    ("Active", "Active"),
    ("Inactive", "Inactive"),
)

Group.add_to_class('description', models.CharField(
    max_length=180, null=True, blank=True))
Group.add_to_class('status', models.CharField(
    max_length=13, choices=STATUS_CHOICES, default='Active'))
class User(AbstractUser):
    groups = models.ForeignKey(
        Group, on_delete=models.SET_NULL, null=True, related_name="groups")
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    status = models.CharField(max_length=13, choices=STATUS_CHOICES, default='Inactive')
    created_on = models.DateTimeField(_('Created Date'), auto_now_add=True)
    updated_on = models.DateTimeField(_('Updated Date'), auto_now=True)
    published = models.BooleanField(_('Published on'), default=True)

    def __str__(self):
        return self.email



