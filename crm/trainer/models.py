from django.db import models

# Create your models here.

from students.models import BaseClass

class Trainer(BaseClass):

    name = models.CharField(max_length=25)


    class Meta:

        verbose_name = 'Trainers'

        verbose_name = 'Trainers'

    def __str__(self):

        return self.name