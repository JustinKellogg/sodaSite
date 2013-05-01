from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from sodaSite.api.models import *
from django.core.mail import send_mail

def my_login(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(username=username, password=password)
  if user is not None:
    login(request, user)
    muser = request.user.machineuser_set.all()
    muser = muser[0]
    return render_to_response('purchase/index.html',
    {'user': muser, 'machine_list': Machine.objects.all()},
    context_instance = RequestContext(request))
  else:
      return render_to_response('purchase/login.html',
      {'error_message': "Invalid username or password"},
      context_instance = RequestContext(request))
  
def index(request):
  if request.user.is_authenticated():
    muser = request.user.machineuser_set.all()
    muser = muser[0]
    machine_list = Machine.objects.all()
    return render_to_response('purchase/index.html',
    {'user': muser, 'machine_list': machine_list},
    context_instance = RequestContext(request))
  else:
    return render_to_response('purchase/login.html', context_instance = RequestContext(request))
    
def my_logout(request):
  logout(request)
  return render_to_response('purchase/login.html',
  {'error_message': "Successfully logged out."},
  context_instance = RequestContext(request))
  
def buy(request):
  slotid = request.POST['slot']
  slot = InventorySlot.objects.get(pk=slotid)
  muser = request.user.machineuser_set.all()
  muser = muser[0]
  soda = slot.soda_set.all()
  soda = soda[0]
  desc = "User %i bought a %s at " % (muser.studentID, soda.name) + str(datetime.now())
  if muser.funds >= soda.cost:
    muser.funds -= soda.cost
    muser.save()
    slot.amount -= 1
    slot.save()
    slot.Machine.lastContact = datetime.now()
    slot.Machine.save(update_fields=['lastContact'])
    if slot.amount < 1:
        send_mail('Out of Stock', "Slot %i of Machine %i has %i sodas left" % (slot.id, slot.Machine.id, slot.amount),
                 'sodaacm@gmail.com', ['jdk998@mst.edu'])           
    trans = SodaTransaction(amount=soda.cost, date_time=datetime.now(), description=desc,
                User=muser, Soda=soda)
    trans.save()
    soda.delete()
    return render_to_response('purchase/index.html',
    {'user': muser, 'machine_list': Machine.objects.all(),
    'purchase': "Soda successfully purchased"},
    context_instance = RequestContext(request))
  else:
    return render_to_response('purchase/index.html',
    {'user': muser, 'machine_list': Machine.objects.all(),
    'purchase': "You don't have enough money"},
    context_instance = RequestContext(request))
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  