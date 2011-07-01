from django.contrib import admin
from models import Location, Job, Person, Status, Esign, Esign_Sys, Purchase, Device 

admin.site.register(Device)
admin.site.register(Location)
admin.site.register(Job)
admin.site.register(Person)
admin.site.register(Status)
admin.site.register(Esign)
admin.site.register(Esign_Sys)
admin.site.register(Purchase)
