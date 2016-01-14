from __future__ import unicode_literals

from django.db import models

class Search(models.Model):
    terms = models.CharField(max_length=255, blank=False)