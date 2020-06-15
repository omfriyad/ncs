from django.shortcuts import render
from django.shortcuts import HttpResponse
from main.models import *
from django.http import JsonResponse
from main.manager import *
import datetime
from django.utils import timezone
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist

"""
This method is responsible for initializing the Node Modules
This method will be call when the node module is connected to the server
this method will receive a post request with the ID and IP of the node module
that has been assigned by the router
"""


def initialize(request):

    if request.method == 'POST':
        try:
            ip = str(request.POST['ip'])
            node_id = int(request.POST['id'])
            obj, created = Node.objects.get_or_create(id=node_id)
            ipt, ipt_created = IpTable.objects.get_or_create(node=obj)
            ipt.ip = ip
            ipt.save()

            print(ip)
            print(node_id)
        except:
            print('error')

    return HttpResponse('')


""" 
This method is responsible to receive the call from a bed/Node Module
It will receive an ID of the call and make a pass it on the internal functions to make call 
to the nurses that has been assigned in the ward
"""

def bed(request):
    if request.method == "POST":
        id = request.POST['id']
        print(id)

        if Bed.objects.filter(node=id).exists():
            bed = Bed.objects.get(node=id)
            call_id = make_call(bed)
            print("CALL ID: ", call_id)
            return HttpResponse(call_id)
            #return JsonResponse({'msg':'success'})
        else:
            return JsonResponse({'msg':'failed | bed doesn\'t exist'})

    return render(request, 'main.html',context={'':''})


"""
This method will be taking the call feed back from nurse and assign the nurse to call
also changing the status of the nurse 
"""


def nurse(request):
    if request.POST:
        node_id = request.POST['id']
        call_id = request.POST['call_id']
        call = Call.objects.get(id=int(call_id))
        print(call.status)
        print("NODE ID: "+node_id)

        if call.status == 'pending':
            n_node = Node.objects.get(id=int(node_id))
            print(n_node)
            nurse = Nurse.objects.get(node=n_node)
            print(nurse.name)
            nurse.status = "busy"
            call.status = "received"
            call.rec_time = datetime.datetime.now(tz=timezone.utc)
            call.nurse = nurse
            call.save()
            nurse.save()
            # alert others -> to be implemented
            alert_others(node_id)
            print(nurse)


    return HttpResponse('None')


"""
This method is for getting the rfid number of the nurse
"""
def attendence(request):
    pass


def rfid(request):
    if request.POST:
        call_id = request.POST['call_id']
        rfid = request.POST['rfid']


        # print('rfid')
        # print(request.POST)
        #
        call = Call.objects.get(id=call_id)
        #
        # print(call.nurse_id)
        # print(call)

        if call.nurse.rfid == rfid:
            print("RFID MATCHED!")
            call.status = "Served"
            call.serv_time = datetime.datetime.now(tz=timezone.utc)
            call.save()
            nurse = call.nurse
            nurse.status = "free"
            nurse.save()

            # nurse2 = Nurse.objects.get(nurse=1)
            # nurse2.status ="free"
            # nurse2.save()
            #
            # nurse2 = Nurse.objects.get(nurse=2)
            # nurse2.status = "free"
            # nurse2.save()

    return HttpResponse("NONE")

"""
This method is for general tasks like getting the time & date from the server to display to the 
Node module 
"""


def general(request):
    if request.POST:
        print(request.POST)

    return HttpResponse('None')


"""
This method is for monitoring all the calls incoming 
"""


def monitor(request):
    context = {"": ""}

    if request.method == "GET":

        calls = Call.objects.all().order_by('-id')
        last_call_id = 0

        try:
            last_call_id = Call.objects.last().id
            print(last_call_id)

            last_call = Call.objects.last()
            print(last_call.rec_time == None)
        except:
            print('failed to get call id')

        context = {
            "calls": calls,
            "last_call_id": last_call_id
        }

        #return JsonResponse({'response': "got you"})

    return render(request, 'call.html', context=context)


def monitor_api(request):
    if request.POST:
        try:
            ajax_call = request.POST['ajax_call']
            id_check = request.POST['last_call_id']
            response_msg = {}

            if ajax_call == "M1o2n3i4t5o6r7i8n9g":

                new_call = Call.objects.last()
                print(new_call)
                print('hola')

                response_msg['response'] = 'Authenticated & succeeded'

                response_msg['call_msg'] = {
                        'id': str(new_call.id),
                        'bed': str(new_call.bed),
                        'nurse': str(new_call.nurse),
                        'call_time': str(new_call.call_time),
                        'rec_time': str(new_call.rec_time),
                        'server_time': str(new_call.serv_time),
                        'status': str(new_call.status),
                }

                if id_check != str(new_call.id):
                    response_msg['call_status'] = 'create'

                elif id_check == str(new_call.id):
                    response_msg['call_status'] = 'update'

                    # if new_call.rec_time != None and new_call.serv_time != None:
                    #     #response_msg['call_status'] = 'nothing'
                    #     return JsonResponse({'response': "Table is already up-to-date!!"})
                        # response_msg['call_status'] = 'nothing'
                return JsonResponse(response_msg)
            else:
                return JsonResponse({'response': "Authentication Failed"})
        except:
            print("call failed")
            return JsonResponse({'response': "call failed"})

    return JsonResponse({'response': "nothing to show"})