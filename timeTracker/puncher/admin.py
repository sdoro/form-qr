from django.contrib import admin

# Register your models here.
from .models import clocking, checkPoint, person

admin.site.register(clocking)
admin.site.register(checkPoint)
admin.site.register(person)
