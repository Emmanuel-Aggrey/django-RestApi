from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

relation = (
    ('mum','Mum'),
    ('sister','Sister'),
    ('brother','Brother'),
    ('friend','Friend'),
)
class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    relationship = models.CharField(max_length=7,choices=relation,null=True)

    def __str__(self):
        return self.name


# signal to generate token on user post request
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
