from djangorestframework.resources import ModelResource
from djangorestframework.reverse import reverse
from contacts.models import Person, PhoneNumber, EmailAddresses, Group, Event

class ContactsResource(ModelResource):
    model = Person
    include = ('numbers','app_id')

#    def phone_numbers(self,instance):
#        if instance.__class__ == PhoneNumber:
#            return instance
#        else:
#            numbers = instance.phonenumber_set.all()
#            return list(numbers)

#    def phone_numbers(self, instance):
#        return reverse('phone_numbers',
#                       kwargs={'contact':instance.id},
#                       request=self.request)

class PhoneNumberResource(ModelResource):
    model = PhoneNumber

#    def contact(self, instance):
#        return reverse('person',
#                       kwargs={'pk':instance.contact.id},
#                       request=self.request)

class EmailAddressResource(ModelResource):
    model = EmailAddresses

class GroupResource(ModelResource):
    model = Group

    def validate_request(self, data, files=None):
        #TODO (julian) change this to handle intelligently uploading masses of data
        if 'persons' in data:
            data['persons'] = [Person.objects.get(pk=1).id]

        return super(GroupResource, self).validate_request(data, files)

class EventResource(ModelResource):
    model = Event


