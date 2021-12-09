from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


def custom_upload_to(instance, filename):
    # Aquí se puede definir la lógica de subida de archivos
    # elimina el archivo anterior
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename # Nuevo archivo


# Create your models here.
class Profile(models.Model):
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE) # relación de 1 a 1 con el modelo User



# Signal to create a profile when a user is created
@receiver(post_save, sender=User)
def ensure_profile_exist(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print('Se acaba de crear un usuario y su perfil también')