from django.db import models
from datetime import datetime
# Create your models here.
class note(models.Model):
    desc=models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)