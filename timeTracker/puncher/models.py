from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class clocking(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.IntegerField()
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField()
