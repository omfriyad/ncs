from django.contrib import admin

from main.models import *
# Register your models here.


admin.site.register(Node)
admin.site.register(Nurse)
admin.site.register(Bed)
admin.site.register(Ward)
admin.site.register(Call)
admin.site.register(IpTable)

