from django.db import models
import string
import random

def codegenerator():
    length =8
    while True:
        code = ''.join(random.choice(string.ascii_letters,k=length))
        if Room.objects.filter(code=code).count()==0:
            break
    return code
# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8,default =codegenerator,unique=True)
    host = models.CharField(max_length=50,unique=True)
    guest_can_pause = models.BooleanField(null = False, default=False)
    votes_to_skip = models.IntegerField(null=False,default=2)
    created_at= models.DateTimeField(auto_now_add=True)
