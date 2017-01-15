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

    def __str__(self):
        return str(self.punch_id)
    
    def was_checkin_recently(self):
        return self.clock_in >= timezone.now() - datetime.timedelta(days=1)
    
    def was_checkout_recently(self):
        return self.clock_out >= timezone.now() - datetime.timedelta(days=1)

class checkPoint(models.Model):
    checkpoint_id = models.IntegerField(primary_key=True)
    
    def __str__(self):
        return str(self.checkpoint_id)

class person(models.Model):
    person_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.person_id)
