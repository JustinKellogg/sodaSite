# Create your views here.
from django.http import HttpResponse, Http404
from sodaSite.api.models import *
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.core.mail import send_mail
from django.utils import simplejson


def transactions(request, soda_id, stid):
#    return render(request, 'api/transactions.html')
    soda = Soda.objects.get(id=soda_id)
    user = MachineUser.objects.get(studentID=stid)
    slot = soda.Slot
    desc = "Is this working"
    if user.funds > soda.cost:
        if slot.amount > 0:
            user.funds -= soda.cost
            user.save()
            slot.amount -= 1
            slot.save()
            slot.Machine.lastContact = datetime.now()
            slot.Machine.save(update_fields=['lastContact'])
            if slot.amount < 1:
                send_mail('Out of Stock', "Test email for transaction",
                         'sodaacm@gmail.com', ['jdk998@mst.edu'])
            trans = SodaTransaction(amount=soda.cost, date_time=datetime.now(), description=desc,
                        User=user, Soda=soda)
            trans.save()
            resp = {'result': 'Success', 'error': 'None'}
            return HttpResponse(simplejson.dumps(resp), mimetype='application/json')
        else:
            resp = {'result':'Failure', 'error': 'Out of inventory'}
            return HttpResponse(simplejson.dumps(resp), mimetype='application/json')
    else:
        resp = {'result': 'Failure', 'error': 'Out of Money'}
        return HttpResponse(simplejson.dumps(resp), mimetype='application/json')


