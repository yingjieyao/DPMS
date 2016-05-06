from __future__ import unicode_literals

from django.db import models

## user model here

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username

class User_info(models.Model):
    user_name = models.CharField(max_length=50)
    user_gender = models.CharField(max_length=50)
    user_hometown = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=50)
    user_idcard = models.CharField(max_length=50)
    user_company = models.CharField(max_length=50)

    def __unicode__(self):
        return str(self.id)

class Room(models.Model):
    building_id = models.IntegerField()
    room_name = models.CharField(max_length=50)
    room_size = models.CharField(max_length=50)
    user_id = models.ForeignKey(User_info)

    def __unicode__(self):
        return self.username

# class Room_user(models.Model):
#     join_time = models.DateField()
#     room_id = models.ForeignKey(Room)
#     user_id = models.ForeignKey(User_info)

class Complaint(models.Model):
    user_id = models.ForeignKey(User_info)
    comp_date = models.DateField()
    comp_content = models.CharField(max_length=256)

class Repair(models.Model):
    user_id = models.ForeignKey(User_info)
    repair_date = models.DateField()
    repair_content = models.CharField(max_length=256)

class Charge(models.Model):
    user_id = models.ForeignKey(User_info)
    charge_date = models.DateField()
    charge_type = models.CharField(max_length=128)
    charge_total = models.FloatField()
    charge_complet = models.FloatField()
    charge_cont = models.CharField(max_length=128)

class Device(models.Model):
    name = models.CharField(max_length=128)
    device_type = models.CharField(max_length=128)
    brand = models.CharField(max_length=128)
    date = models.DateField()

    def __unicode__(self):
        return self.name

class Device_repair(models.Model):
    device_id = models.ForeignKey(Device)
    repair_date = models.DateField()
    repair_content = models.CharField(max_length=128)

class Accident(models.Model):
    device_id = models.ForeignKey(Device)
