from django.db import models
from django.utils.translation import ugettext_lazy as _
from .choices import SHAPE_CHOICE
from django.core.mail import send_mail
from tables.settings import EMAIL_HOST_USER


""" Hall base model - input data from admin panel """
class Hall(models.Model):

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        null=True,
        blank=True,
    )

    # input in metres 
    width = models.FloatField(
        verbose_name=_('Width in metres'),
    )

    #input in metres
    length = models.FloatField(
        verbose_name=_('Length in metres'),
    )

    def __str__(self):
        return f'{self.name}: width {self.width}, length {self.length}'

""" 
    Table base model related to Hall width and leangth stored in float number 
                        representing percetns 
"""
class Table(models.Model):
    number = models.PositiveSmallIntegerField(
        verbose_name=_('Number'),
    )

    placements = models.PositiveSmallIntegerField(
        verbose_name=_('Placements'),
    )

    shape = models.PositiveSmallIntegerField(
        verbose_name=_('Placements'),
        choices=SHAPE_CHOICE,
    )

    width = models.FloatField(
        verbose_name=_('Width in metres'),
    )

    length = models.FloatField(
        verbose_name=_('Length in metres'),
    )

    xlocation = models.FloatField(
        verbose_name=_('X Position in percents'),
        null=True,
        blank=True,
    )

    ylocation = models.FloatField(
        verbose_name=_('Y Position in percents'),
        null=True,
        blank=True,
    )

    hall = models.ForeignKey(
        to=Hall,
        verbose_name=_('Hall'),
        on_delete=models.CASCADE,
        related_name='hall',
    )

    def __str__(self):
        return f'{self.number}: placements {self.placements}, shape {self.shape}'

    def save(self, **kwargs):
        self.width = round((self.width / self.hall.width)*100, 2)
        self.length = round((self.length / self.hall.length)*100, 2)
        return super().save(**kwargs)


""" Reservation table related to table """    
class Reservation(models.Model):
    table = models.ForeignKey(
        to=Table,
        verbose_name=_('Table'),
        on_delete=models.CASCADE,
        related_name='table',
    )

    client_name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
    )

    email = models.EmailField(
        verbose_name=_('Email'),
        max_length=128,
    )

    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=12,
    )

    comment = models.TextField(
        verbose_name=_('Comment'),
        blank=True,
    )

    reservation_date = models.DateTimeField(
        verbose_name=_('Reservation Date'),
    )

    """ Only one reservation per table """
    class Meta:
        unique_together = ('table', 'reservation_date',)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_mail(
            'Subject here',
            'Here is the message.',
            EMAIL_HOST_USER,
            [self.email,],
            fail_silently=False,
        )

    def __str__(self):
        return f'{self.table}: client {self.client_name}, date {self.reservation_date}'