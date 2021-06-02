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
        
        

class Item(models.Model):
    status=[
        ['Active', 'Active'],
        ['In_Active', 'In Active'],
        ['Dead','Dead'],
    ]

    node=[
        ['PC', 'PC'],
        ['PHONE', 'PHONE'],
        ['PRINTER','PRINTER'],
        ['DLINK_SWITCH','DLINK SWITCH'],
        ['CISCO_SWITCH','CISCO SWITCH'],
    ]
    note = models.CharField(max_length=200,null=True,blank=True,help_text='just not to confuse each other any descriptive text')
    brand = models.CharField(max_length=200)
    model_no = models.CharField(max_length=200,blank=True,null=True,help_text="wmic computersystem get model,name")
    serial_no = models.CharField(max_length=200,null=True,blank=True,unique=True,help_text='wmic bios get serialnumber')
    node_name= models.CharField(max_length=200,null=True,blank=True,help_text='wmic computersystem get name')
    type_of_computer = models.CharField(max_length=200,blank=True,null=True,choices=node)
    processor = models.CharField(max_length=200,null=True,blank=True)
    ram_size = models.CharField(max_length=200,null=True,blank=True)
    hdd_size = models.CharField(max_length=200,null=True,blank=True)
    ip_address= models.GenericIPAddressField(unique=True,null=True,blank=True)
    location = models.CharField(max_length=200,null=True,blank=True)

    status =models.CharField(max_length=20,null=True,blank=True,choices=status)
    assiend_end_user= models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return f'{self.brand} {self.brand}'


   
