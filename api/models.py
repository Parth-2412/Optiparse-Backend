from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

fs = FileSystemStorage(location=settings.MEDIA_ROOT + 'uploads')

# Create your models here.

class Uploads(models.Model):
    file = models.ImageField(storage=fs)



@receiver(post_delete, sender=Uploads)
def photo_post_delete_handler(sender, **kwargs):
    photo = kwargs['instance']
    storage, path = photo.file.storage, photo.file.path
    storage.delete(path)