# Create your views here.
from django.http import HttpResponse, Http404
from sodaSite.api.models import *
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.utils import simplejson, timezone
from sodaSite.settings import ADMINS


# def transactions(request, soda_id, stid):
    # TODO: Check that request comes from raspberry pi's
    # soda = Soda.objects.get(id=soda_id)
    # try:
        # user = MachineUser.objects.get(studentID=stid)
    # except:
        # TODO narrow down exception
        # ip = request.META.get('HTTP_X_FORWARDED_FOR')
        # ip = request.META.get('REMOTE_HOST')
        # ip = request.user
        # response = {'result': 'failure', 'error': 'Student id does not exist '+ str(ip)}
        # return HttpResponse(simplejson.dumps(response), mimetype='application/json')
    # slot = soda.Slot
    # desc = "User %i bought a %s at " % (user.studentID, soda.name) + str(datetime.now())
    # if user.funds >= soda.cost:
        # if slot.amount > 0:
            # user.funds -= soda.cost
            # user.save()
            # slot.amount -= 1
            # slot.save()
            # slot.Machine.lastContact = datetime.now()
            # slot.Machine.save(update_fields=['lastContact'])
            # if slot.amount < 1:
                # send_mail('Out of Stock', "Slot %i of Machine %i has %i sodas left" % (slot.id, slot.Machine.id, slot.amount),
                         # 'sodaacm@gmail.com', ['jdk998@mst.edu'])
            # trans = SodaTransaction(amount=soda.cost, date_time=datetime.now(), description=desc,
                        # User=user, Soda=soda)
            # trans.save()
            # resp = {'result': 'Success', 'error': 'None'}
            # return HttpResponse(simplejson.dumps(resp), mimetype='application/json')
        # else:
            # resp = {'result': 'Failure', 'error': 'Out of inventory'}
            # return HttpResponse(simplejson.dumps(resp), mimetype='application/json')
    # else:
        # resp = {'result': 'Failure', 'error': 'Out of Money'}
        # return HttpResponse(simplejson.dumps(resp), mimetype='application/json')


def ping_machine(request, m_id):
    try:
        machine = Machine.objects.get(id=m_id)
    except:
        response = {'result': 'failure', 'error': 'machine does not exist'}
        return HttpResponse(simplejson.dumps(response), mimetype='application/json')
    machine.lastContact = datetime.now()
    machine.save(update_fields=['lastContact'])


def check_machine(request):
    response = {}
    for machine in Machine.objects.all():
        if machine.lastContact < timezone.now() - timedelta(minutes=10):
            send_mail('Machine down',"Machine %i at %s is out of contact" % (machine.id, machine.location),'sodaacm@gmail.com',[admin[1] for admin in ADMINS])
            response = {'result':'failure', 'error': 'Machine out of contact'}
    return HttpResponse(simplejson.dumps(response), mimetype='application/json')
