from django.db import models
from django.contrib.flatpages.models import FlatPage

# Create your models here.

DEQUEM =([1,"Dri"], [2,"Li"], [3,"Neide"], [4,"Bia"])

class Convite(models.Model):
    nome = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    convidados = models.FloatField(null=True, blank=True)
    convites = models.IntegerField(null=True, blank=True)
    dequem = models.IntegerField(choices=DEQUEM, null=True, blank=True)
    rspv = models.DateTimeField(null=True, blank=True)
    adultos = models.IntegerField(null=True, blank=True)
    criancas = models.IntegerField(null=True, blank=True)

from django.contrib.comments.moderation import  moderator 
from comments_spamfighter.moderation import SpamFighterModerator
class PostModerator(SpamFighterModerator):
    # django's genric moderation options
    #auto_moderate_field = 'created'
    email_notification = True

    # comments spamfighter options
    akismet_check = True
    akismet_check_moderate = True
    keyword_check = True
    keyword_check_moderate = False


#PLEASE PLEASE don't kill me Niemeyer
if not (FlatPage in moderator._registry) :
    moderator.register(FlatPage, PostModerator)

