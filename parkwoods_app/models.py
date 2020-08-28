from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime

# Create your models here.

class Topic(models.Model):
    """ topic user is learning """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."


class Division(models.TextChoices):
    TYKE = 'TK', _('Tyke')
    MINOR_NOVICE = 'MN', _('Minor Novice')
    NOVICE = 'NV', _('Novice')
    MINOR_ATOM = 'MA', _('Minor Atom')
    ATOM = 'AT', _('Atom')
    MINOR_PEEWEE = 'MP', _('Minor Peewee')
    PEEWEE = 'PW', _('Peewee')
    MINOR_BANTAM = 'MB', _('Minor Bantam')
    BANTAM = 'BT', _('Bantam')
    MINOR_MIDGET = 'MM', _('Minor Midget')
    MIDGET_JUNIOR = 'MJ', _('Midget Junior')
    MIDGET_SENIOR = 'MS', _('Midget Senior')
    UNDER_21 = 'UD', _('Under 21')


class Season(models.TextChoices):
    FINAL_2020 = 'FN20', _('FINAL 2020')
    SEMI_FINAL_2020 = 'SF20', _('SEMI-FINAL 2020')
    PLAYOFF_2020 = 'PL20', _('Playoff 2020')
    WINTER_2020 = 'WY20', _('Winter Season 2020')
    FALL_2019 = 'FY19', _('Fall Season 2019')    


class Level(models.TextChoices):
    TIER1 = 'T1', _('Tier 1')
    TIER2 = 'T2', _('Tier 2')
    TIER3 = 'T3', _('Tier 3')
    
class Group(models.TextChoices):
    GROUP_A = 'G1', _('Group A')
    GROUP_B = 'G2', _('Group B')


class Schedule(models.Model):
    game_dt = models.DateField()
    game_time = models.TimeField()
    away = models.CharField(max_length=30)
    home = models.CharField(max_length=30)
    score = models.CharField(max_length=5)
    venue = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    division = models.CharField(
        max_length=2,
        choices=Division.choices,
        default=Division.MIDGET_SENIOR
    )

    season = models.CharField(
        max_length=4,
        choices=Season.choices,
        default=Season.WINTER_2020
    )

    level = models.CharField(
        max_length=2,
        choices=Level.choices,
        default=Level.TIER1
    )

    def save(self, *args, **kwargs):
        self.date_added = datetime.now()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.away + '-' + self.home

class Standings(models.Model):
    name = models.CharField(max_length=30)
    gp = models.IntegerField(editable=False, default=0)
    pts = models.IntegerField(editable=False, default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    gf = models.IntegerField(default=0)
    ga = models.IntegerField(default=0)
    gfavg = models.DecimalField(
        max_digits=5, decimal_places=4, editable=False, default=0.0000)
    date_added = models.DateTimeField(auto_now_add=True)
    
    division = models.CharField(
        max_length=2,
        choices=Division.choices,
        default=Division.MIDGET_SENIOR
    )

    season = models.CharField(
        max_length=4,
        choices=Season.choices,
        default=Season.WINTER_2020
    )

    level = models.CharField(
        max_length=2,
        choices=Level.choices,
        default=Level.TIER1
    )    
    pl_group = models.CharField(
        max_length=2,
        choices=Group.choices,
        default=None, 
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        self.date_added = datetime.now()
        self.pts = self.wins*2 + self.ties
        if self.gf + self.ga == 0:
            self.gfavg = 0.0
        else:
            self.gfavg = self.gf / (self.gf + self.ga)
        self.gp = self.wins + self.ties + self.loses
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
