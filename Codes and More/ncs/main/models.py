from django.db import models

# Create your models here.


class Node(models.Model):

    def __str__(self):
        return 'Node: ' + str(self.id) + ' Usage:' + str(self.used_in)

    @property
    def used_in(self):
        try:
            if self.bed:
                return 1
        except:
            try:
                if self.nurse:
                    return 2
            except:
                return 0


class IpTable(models.Model):
    node = models.OneToOneField(Node, on_delete=None)
    ip = models.CharField(max_length=25, blank=True, default='')

    def __str__(self):
        return 'IP: ' + str(self.ip)


class Ward(models.Model):
    ward = models.IntegerField()

    def __str__(self):
        return 'Ward: ' + str(self.ward)


class Bed(models.Model):
    node = models.OneToOneField(Node, on_delete=None)
    bed = models.IntegerField()
    ward = models.ManyToManyField(Ward)

    def __str__(self):
        return 'Bed: ' + str(self.bed) +' '+str(self.node)

    # def save(self):
    #     if self.node.used_in == 0:
    #         self.save()
    #     else:
    #         raise AttributeError


class Nurse(models.Model):

    name = models.CharField(max_length=90)
    rfid = models.CharField(max_length=15)
    nurse = models.IntegerField()
    node = models.OneToOneField(Node, on_delete=None)
    ward = models.ManyToManyField(Ward)
    status = models.CharField(max_length=10) # free buys leave

    def __str__(self):
        return str(self.name)

    # def save(self):
    #     if self.node.used_in == 0:
    #         self.save()
    #     else:
    #         raise AttributeError


class Call(models.Model):
    bed = models.ForeignKey(Bed, on_delete=None, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True) # BED->Pending NURSE->Received RFID->Served
    nurse = models.ForeignKey(Nurse, on_delete=None, blank=True, null=True)
    call_time = models.DateTimeField(blank=True,null=True)
    rec_time = models.DateTimeField(blank=True, null=True)
    serv_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'Call Time: ' + str(self.call_time) + str(self.bed)



