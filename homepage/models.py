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
        else:
            return ('Banner ' + str(self.pk))
            
            
class Logo(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='Logo', null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    class Meta:
        verbose_name = 'Logo'
    
    def __str__(self):
        if (self.name):
            return self.name
        else:
            return ('Logo '+ str(self.pk))
            
            
class WorkingArea(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='Working Areas', null=True, blank=True)
    publish = models.BooleanField(default=False, help_text='check me to show this in home page')
    recent_work = models.BooleanField(default=False, help_text='check me to display as recent work')
    created = models.DateTimeField(auto_now_add=False, auto_now=True)
    published = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.title 
        
            
class Footer(models.Model):
    org_name = models.CharField('organization Full Name', max_length=140, help_text='Write Full Name of Organization')
    address = models.CharField('Organization Full Adress', max_length=140, help_text='eg. Sanepa, Lalitpur')
    country = models.CharField(max_length=50, help_text='Nepal')
    phone = models.IntegerField('Organization Phone Number')
    phone_2 = models.IntegerField('Organization Phone Number 2', null=True, blank=True)
    email = models.EmailField('Organization Email Adress')
    email_2 = models.EmailField('Organization Email Adress', null=True, blank=True)
    
    copyright = models.CharField(max_length=150, help_text='2016 All right reserved By Organization Name')
    
    def __str__(self):
        return self.org_name
        
        
class SocialMediaIcon(models.Model):
    name = models.CharField('social Media Name', max_length=20, help_text='e.g. Facebook, Twetter, Youtube')
    url = models.URLField(max_length=200, help_text='https://www.facebook.com/pagename')
    icon = models.ImageField(upload_to='Social Media Icon', null=True, blank=True)
    
    def __str__(self):
        return self.name
        