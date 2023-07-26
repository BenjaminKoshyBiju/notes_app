from django.db import models
from django.utils import timezone
timezone.localtime(timezone.now())
# from datetime import datetime
# Create your models here.
class note(models.Model):
    desc=models.TextField()
    date = models.DateTimeField( default=timezone.now, blank=True)