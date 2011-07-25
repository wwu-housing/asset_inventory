import datetime

from django.db import models


class Location(models.Model):
    Building_Choices = (
        (u'BW', u'Birnam Wood'),
        (u'BT', u'Buchannan Towers'),
        (u'CM', u'Commisary'),
        (u'EA', u'Edens Administration'),
        (u'EN', u'Edens North'),
        (u'EH', u'Edens South'),
        (u'FA', u'Fairhaven College'),
        (u'FC', u'Fairhaven Commons'),
        (u'FX', u'Fairhaven Stacks'),
        (u'HI', u'Highland'),
        (u'HG', u'Higginson'),
        (u'MA', u'Mathes'),
        (u'NA', u'Nash'),
        (u'PP', u'Physical Plant'),
        (u'RA', u'Ridge Alpha'),
        (u'RB', u'Ridge Beta'),
        (u'RC', u'Ridge Commons'),
        (u'RD', u'Ridge Delta'),
        (u'RG', u'Ridge Gamma'),
        (u'RK', u'Ridge Kappa'),
        (u'RO', u'Ridge Omega'),
        (u'RS', u'Ridge Sigma'),
        (u'VC', u'Viking Commons'),
        (u'VU', u'Viking Union'),
    )
    Location_Options = (
        (u'A', u'Administrative'),
        (u'C', u'Computer Lab'),
    )
    
    building = models.CharField(max_length=3, choices=Building_Choices)
    location_type = models.CharField(max_length=1, choices=Location_Options)
    room = models.CharField(max_length=10)
    station_location = models.CharField(max_length=30, blank=True)
    lock_type = models.CharField(max_length=50)
    is_deleted = models.BooleanField()

    @property
    def get_building_name(self):
        return dict(self.Building_Choices).get(self.building)
    def get_location_type(self):
        return dict(self.Location_Options).get(self.location_type)

    class Meta:
        verbose_name_plural = "Locations"

    def __unicode__(self):
        if (self.location_type == "C"):
            b = ", Lab Station #: " + self.station_location
        else:
            b = ""
        return u'%s %s %s' % (self.get_building_name, self.room, b)

        
class Job(models.Model):
    title = models.CharField(max_length=150)
    unit = models.CharField(max_length=150)
    is_deleted = models.BooleanField()
    
    class Meta:
        verbose_name_plural = "Jobs"
    def __unicode__(self):
        return u'%s, %s' % (self.title, self.unit)


class Person(models.Model):
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    job_info = models.ForeignKey(Job)
    is_deleted = models.BooleanField()

    @property
    def name(self):
        return u'%s %s' % (self.first_name, self.last_name)
    
    def __unicode__(self):
        return u'%s %s, %s' % (self.first_name, self.last_name, self.job_info.title)
    class Meta:
        verbose_name_plural = "People"


class Status(models.Model):
    status = models.CharField(max_length=100)
    description = models.TextField()
    is_deleted = models.BooleanField()

    class Meta:
        verbose_name_plural = "Status Types"
    def __unicode__(self):
        return self.status


class Esign(models.Model):
    esign_type = models.CharField(max_length=100)
    esign_number = models.CharField(max_length=100)
    esign_reason = models.TextField()
    is_deleted = models.BooleanField()
    
    def __unicode__(self):
        return self.esign_number
    class Meta:
        verbose_name_plural = "Esign Forms"


class Purchase(models.Model):
    warranty = models.CharField(max_length=255)
    purchase_date = models.DateField()
    subject = models.CharField(max_length=40)
    description = models.TextField()
    is_deleted = models.BooleanField()

    def __unicode__(self):
        return u'%s, %s' % (self.subject, self.purchase_date)
    class Meta:
        verbose_name_plural = "Purchases"


class Device(models.Model):
    hostname = models.CharField(max_length=255)
    serial = models.CharField(max_length=255)
    state_id = models.CharField(max_length=255)
    teamviewer_ID = models.CharField(max_length=100, verbose_name='Teamviewer ID')
    ram = models.CharField(max_length=100)
    dualscreen = models.BooleanField()
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    proc = models.CharField(max_length=200)
    x64 = models.BooleanField()
    purchase_ID = models.ForeignKey(Purchase)
    Location_ID = models.ForeignKey(Location)
    Person_ID = models.ForeignKey(Person)
    Status_ID = models.ForeignKey(Status)
    last_update = models.DateField(auto_now=True)
    is_deleted = models.BooleanField()

    def __unicode__(self):
        return u'Station: %s in %s %s' % (self.Location_ID.station_location, self.Location_ID.get_building_name, self.Location_ID.room)
    class Meta:
        ordering = ['Location_ID__location_type', 'Location_ID__building']
        verbose_name_plural = "Devices"


class Esign_Sys(models.Model):
    sys_ID = models.ForeignKey(Device)
    esign_ID = models.ForeignKey(Esign)
    is_deleted = models.BooleanField()

    def __unicode__(self):
        return U'%s, Esign#: %s' % (self.sys_ID, self.esign_ID)
    class Meta:
        verbose_name_plural = "Esign to Device Connection Listing"
