from __future__ import unicode_literals

from django.db import models

# Create your models here.
class trackdata(models.Model):
    p_name = models.CharField(max_length=30,default='')
    p_email = models.EmailField(primary_key=True,unique=True)
    p_status = models.CharField(max_length=15)
    p_url = models.CharField(max_length=250,default='')

    def __str__(self):
        return self.p_email
