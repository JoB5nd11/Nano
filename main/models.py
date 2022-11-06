from django.db import models

class VideoContent(models.Model):
    media = models.FileField(upload_to='')