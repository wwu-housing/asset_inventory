from django.contrib import admin
from models import Location, Job, Person, Status, Esign, Esign_Sys, Purchase, Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = ("hostname", "serial", "state_id", "teamviewer_ID", "ram",
                    "dualscreen", "brand", "model", "proc", "x64",
                    "purchase_ID", "Location_ID", "station_location",
                    "Person_ID", "Status_ID", "last_update", "is_deleted")

    def station_location(self, obj):
        return obj.Location_ID.station_location
admin.site.register(Device, DeviceAdmin)


admin.site.register(Location)
admin.site.register(Job)
admin.site.register(Person)
admin.site.register(Status)
admin.site.register(Esign)
admin.site.register(Esign_Sys)
admin.site.register(Purchase)
