from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''Ref: http://www.tangowithdjango.com/book/chapters/login.html'''

class UserProfile(models.Model):
    '''Links UserProfile to User model instance'''
    user = models.OneToOneField(User)
    
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    '''Override the __unicode__() method to return out somthing meaningful'''
    def __unicode__(self):
        return self.user.name