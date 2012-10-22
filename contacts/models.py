from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField
# Create your models here.
from djangorestframework.resources import ModelResource

PHONE_NUMBER_CHOICES = (
    (u'1', 'Home'),
    (u'2', 'Work'),
    (u'3', 'Mobile')
)

EMAIL_CHOICES = (
    (u'1', 'Personal'),
    (u'2', 'Work'),
)
class Person(models.Model):

    fb_id = models.CharField(max_length=60)
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    lkdin_id = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos') #avatar
    on_phone = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s, %s' % (self.last, self.first)

    def app_id(self):
        return self.id
    def numbers(self):
        numbers = self.phonenumber_set.all()
        def make_number_dict(arg):
            number_dict = dict()
            number_dict['type'] = arg.type
            number_dict['phone'] = arg.phone
            return number_dict
        number_list = map(make_number_dict,list(numbers))
        return number_list
        #return {'test':'test'}

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
    # TODO (julian) may want to generate and save an ics file

class EmailAddresses(models.Model):
    type = models.CharField(max_length=1, choices=EMAIL_CHOICES)
    contact = models.ForeignKey(Person)
    email = models.EmailField()

class PhoneNumber(models.Model):
    type = models.CharField(max_length=1, choices=PHONE_NUMBER_CHOICES)
    phone = PhoneNumberField()
    contact = models.ForeignKey(Person)


