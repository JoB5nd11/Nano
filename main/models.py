from django.db import models
from django.conf import settings
from django.utils import timezone
import os

class VideoContent(models.Model):
    media = models.FileField(upload_to='')
    datetime = models.DateTimeField(default=timezone.now())