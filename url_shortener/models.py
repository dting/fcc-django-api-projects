from __future__ import unicode_literals

from django.db import models

class ShortUrl(models.Model):
    long_url = models.TextField(blank=False)
