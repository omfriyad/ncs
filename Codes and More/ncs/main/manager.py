from time import sleep
from main.models import *
import requests
import datetime
from django.utils import timezone


def get_ip(node):
    ipt = IpTable.objects.filter(node=node)
    return ipt[0].ip


def nurse_status(nurse):
    if nurse.status == 'free':
        return True
    else:
        return False


def make_call(bed):
    nurses = Nurse.objects.filter(ward=bed.ward.get())
    ips = []
    for nurse in nurses:
        if nurse_status(nurse):
            ips.append(get_ip(nurse.node))

    print("Making call from BED: " + str(bed.id))
    print("Assigned Nurse IPs:", ips)

    if len(ips) >0:
        call = Call.objects.create()
        call.bed = bed
        call.call_time = datetime.datetime.now(tz=timezone.utc)
        call.status = 'pending'
        call_id = call.id
        call.save()
        print("CALL ID FROM MAEK: " + str(call_id))

        # call_id_to_bed(get_ip(bed.node), call.id)
        call_nurse_node(bed, ips, call.id)
        return call_id
    else:                        # Wait some times
        sleep(300)
        return make_call(bed)


def call_id_to_bed(ip, call_id):

    data = {'sc': "123456789",
            'call_id': call_id}

    ip = "http://" + ip + "/"

    try:
        print("Sending bed: " + ip)
        requests.post(url=ip, data=data, timeout=2)
    # except requests.exceptions.HTTPError as err:
    #     print(err)
    except:
            print("unable to send post to patient")


def call_nurse_node(bed, ips, call_id):

    data = {'sc': "123456789",
            'bed_id': bed.id,
            'call_id': call_id}

    for ip in ips:
        ip = "http://" + ip + "/"
        try:
            print("Calling IP: " + ip)
            r = requests.post(url=ip, data=data, timeout=1.5)
            print(r)
        except:
            pass


def alert_others(node_id):
    node = Node.objects.get(id=node_id)
    nurse = Nurse.objects.get(node=node)
    ward = Ward.objects.get(nurse=nurse) # get_ward
    nurses = Nurse.objects.filter(ward=ward).exclude(id=nurse.id)
     # get nodes of the nurses  # exclude the currrent node
    data = {
        'sc': '123456789',
        'choice': '1',
        'msg': "Call answered by " + nurse.name
    }
    for n in nurses:
        try:    # send alert #get their ips
            ip = "http://" + n.node.iptable.ip + "/alert"
            requests.post(ip, data, timeout=2)
        except:
            print("alert failed")

