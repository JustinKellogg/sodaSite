from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.


class Soda(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    sugar = models.IntegerField(help_text="measured in grams")
    calories = models.IntegerField()
    description = models.CharField(max_length=200)
    slot = models.ForeignKey(InventorySlot)
    cost = models.IntegerField(help_text="Measured in pennies. ex: 100 = $1")

    def __unicode__(self):
        return self.name


class InventorySlot(models.Model):
    slotID = models.IntegerField(primary_key=True)
    amount = models.IntegerField()
    sodaType = models.CharField(max_length=20)
    machine = models.ForeignKey(Machine)
    revenue = models.IntegerField()

    def __unicode__(self):
        return self.sodaType


class Machine(models.Model):
    location = models.CharField(max_length=100, unique=True,
                                help_text="describes where the machine is. (Building Room Floor) ex: CS 213 1")
    heatGood = models.BooleanField()
    machineID = models.IntegerField(primary_key=True)
    revenue = models.IntegerField()

    def __unicode__(self):
        return self.machineID