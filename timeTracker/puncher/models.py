from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class clocking(models.Model):
    punch_id = models.AutoField(primary_key=True)
    checkPoint_id = models.IntegerField()
    person_id = models.IntegerField()
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField()

class checkPoint(models.Model):
    checkpoint_id = models.IntegerField(primary_key=True)

class person(models.Model):
    person_id = models.IntegerField(primary_key=True)
