from django.test import TestCase
from django.test.client import Client
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from sodaSite.api.models import Machine, InventorySlot, MachineUser, Soda, Transaction, SodaTransaction
from datetime import datetime
from django.contrib.auth.models import User

class PurchaseMethodTests(TestCase):
  def test_login(self):
    client = Client()
    user = User.objects.create_user(username='jerry', password='1234')
    
    response = client.post('/purchase/', {'username': 'jerry', 'password': '1234'})
    
    self.assertEqual(user.is_authenticated(), True)
    
    
    
  def test_buy(self):
    client = Client()
    user = User.objects.create_user(username='jerry', password='1234')
    client.login(username='jerry', password='1234')
    
    m = Machine.objects.create(location="a", heatGood=True, lastContact=datetime.now(), Admin=user)
    slot = InventorySlot.objects.create(amount=2, sodaType="MD", Machine=m)
    u = MachineUser.objects.create(User=user, studentID=1, funds=100)
    Soda.objects.create(name="MD", sugar=0, calories=0, description="", Slot=slot, cost=100)
    
    #buy a soda
    response = client.post('/purchase/buy', {'slot': 1})

    self.assertEqual(response.status_code, 200)
    self.assertEqual(SodaTransaction.objects.get(pk=1).amount, 100)
    self.assertEqual(InventorySlot.objects.get(pk=1).amount, 1)
    self.assertEqual(MachineUser.objects.get(pk=1).funds, 0)
    
    #try to buy a soda with no money
    response = client.post('/purchase/buy', {'slot': 1})

    self.assertEqual(response.status_code, 200)
    self.assertEqual(InventorySlot.objects.get(pk=1).amount, 1)
    self.assertEqual(MachineUser.objects.get(pk=1).funds, 0)