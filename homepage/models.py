from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True, help_text='Give beautiful title')
    description = models.TextField(null=True, blank=True,  help_text='write short and sweet description related to your title')
    image = models.ImageField(upload_to='Banner/%Y-%m-%d')
    publish = models.BooleanField(default=False,help_text='check me to show this banner image in home page')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        if (self.title):
            return self.title
        