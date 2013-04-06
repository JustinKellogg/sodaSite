from django.db import models
from django.contrib.auth.models import User as AuthUser
from sodaSite.api.sodaTypes import SODA_TYPE_CHOICES
from datetime import datetime
from django.core.mail import send_mail

# Create your models here.
class Machine(models.Model):
    location = models.CharField(max_length=100, unique=True,
                                help_text="describes where the machine is. (Building Floor) ex: CS 1")
    heatGood = models.BooleanField()
    machineID = models.IntegerField(primary_key=True)
    lastContact = models.DateTimeField(auto_now_add=True, help_text="Tells last time machine contacted Database.")
    Admin = models.ForeignKey(AuthUser)

    def __str__(self):
        return str(self.machineID)

class InventorySlot(models.Model):
    slotID = models.IntegerField(primary_key=True)
    amount = models.IntegerField()
    sodaType = models.CharField(max_length=20)
    Machine = models.ForeignKey(Machine)

    class Meta:
        ordering = ['slotID']

    def __str__(self):
        return "Slot %d: %d units of %s" % (self.slotID, self.amount, self.soda.name)

class Client(models.Model):
    auth_key = models.CharField(max_length=200)
    name = models.CharField(max_length=30,primary_key=True)

class MachineUser(models.Model):
    User = models.ForeignKey(AuthUser,primary_key=True)
    studentID = models.IntegerField()
    funds = models.IntegerField(help_text="Measured in pennies",default=0)

    def __str__(self):
        return self.User.username

class Soda(models.Model):
    name = models.CharField(max_length=5, choices=SODA_TYPE_CHOICES)
    sugar = models.IntegerField(help_text="measured in grams")
    calories = models.IntegerField()
    description = models.CharField(max_length=200)
    Slot = models.ForeignKey(InventorySlot)
    cost = models.IntegerField(help_text="Measured in pennies. ex: 100 = $1")

    def __str__(self):
        return self.name

class Transaction(models.Model):
    amount = models.IntegerField(help_text="Measured in pennies")
    date_time = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    User = models.ForeignKey(MachineUser)

    class Meta:
        ordering = ['-date_time']

class AdminTransaction(Transaction):
    Admin = models.ForeignKey(AuthUser)

    def __str__(self):
        return self.Admin.first_name,"did something to", str(self.User.studentID)

class SodaTransaction(Transaction):
    Soda = models.ForeignKey(Soda)

    def __str__(self):
        return str(self.User.studentID), "bought a ", Soda.name

class Discount(models.Model):
    name = models.CharField(max_length="200")
    Soda = models.ForeignKey(Soda)
    offset = models.FloatField(help_text="determines percent off. i.e .3 is 30% off")
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    def __str__(self):
        return self.name

adminable = [Discount, Soda, SodaTransaction, AdminTransaction, Transaction, Machine, MachineUser, InventorySlot]
