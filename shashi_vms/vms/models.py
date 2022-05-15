from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.core.validators import RegexValidator

# Create your models here.

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

Type = (
    ("Two wheelers", "Two wheelers"),
    ("There wheelers", "There wheelers"),
    ("Four wheelers", "Four wheelers"),
)

class VihicleData(models.Model):
    vehicle_number = models.CharField(max_length=50, unique=True,blank=True,null=True, validators=[alphanumeric])
    vehicle_type = models.CharField(max_length=13, choices=Type, blank=True,null=True)
    vehicle_model = models.CharField(max_length=50, blank=True,null=True)
    vehicle_description = models.TextField(blank=True,null=True)
    created_on = models.DateTimeField(_('Created Date'), auto_now_add=True)
    updated_on = models.DateTimeField(_('Updated Date'), auto_now=True)
    published = models.BooleanField(_('Published on'), default=True)

    def __str__(self):
        return self.vehicle_number