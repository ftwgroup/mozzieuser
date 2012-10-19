from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField
# Create your models here.
from djangorestframework.resources import ModelResource

PHONE_NUMBER_CHOICES = (
    (u'1', 'Home'),
    (u'2', 'Work'),
    (u'3', 'Mobile')
)

class Person(models.Model):
    fb_id = models.CharField(max_length=60)
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    lkdin_id = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos') #avatar
    emails = models.ForeignKey('EmailAddresses')
    on_phone = models.BooleanField(default=True)

class Group(models.Model):
    name = models.CharField(max_length=255)
    persons = models.ManyToManyField(Person)

class Event(models.Model):
    attendees = models.ManyToManyField(Person)
    groups = models.ManyToManyField(Group)
    uuid = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    # TODO (julian) there maybe more fields we need

class EmailAddresses(models.Model):
    primary = models.EmailField()
    secondary = models.EmailField()
    ternary = models.EmailField()

class PhoneNumber(models.Model):
    type = models.CharField(max_length=1, choices=PHONE_NUMBER_CHOICES)
    phone = PhoneNumberField()

class ContactsResource(ModelResource):
    model = Person
