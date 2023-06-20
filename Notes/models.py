from django.db import models
from django.contrib.auth.models import User


# Create your models here.

def media_storage(instance, filename):
    return f'uploads/{instance.user.username}/{instance.note_type}/{filename}'

class Note(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    note_type = models.CharField(choices=(('TEXT','TEXT'),('AUDIO','AUDIO'),('DOCUMENT','DOCUMENT')),default="DOCUMENT",max_length=12)
    file = models.FileField(upload_to=media_storage,null=True,blank=True)
    text = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Notes'
