# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'EmailAddresses.secondary'
        db.delete_column('contacts_emailaddresses', 'secondary')

        # Deleting field 'EmailAddresses.ternary'
        db.delete_column('contacts_emailaddresses', 'ternary')

        # Deleting field 'EmailAddresses.primary'
        db.delete_column('contacts_emailaddresses', 'primary')

        # Adding field 'EmailAddresses.type'
        db.add_column('contacts_emailaddresses', 'type',
                      self.gf('django.db.models.fields.CharField')(default='1', max_length=1),
                      keep_default=False)

        # Adding field 'EmailAddresses.contact'
        db.add_column('contacts_emailaddresses', 'contact',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['contacts.Person']),
                      keep_default=False)

        # Adding field 'EmailAddresses.email'
        db.add_column('contacts_emailaddresses', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='default@example.com', max_length=75),
                      keep_default=False)

        # Adding field 'PhoneNumber.contact'
        db.add_column('contacts_phonenumber', 'contact',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['contacts.Person']),
                      keep_default=False)

        # Deleting field 'Person.emails'
        db.delete_column('contacts_person', 'emails_id')

        # Adding field 'Person.on_phone'
        db.add_column('contacts_person', 'on_phone',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'EmailAddresses.secondary'
        db.add_column('contacts_emailaddresses', 'secondary',
                      self.gf('django.db.models.fields.EmailField')(default='default@example.com', max_length=75),
                      keep_default=False)

        # Adding field 'EmailAddresses.ternary'
        db.add_column('contacts_emailaddresses', 'ternary',
                      self.gf('django.db.models.fields.EmailField')(default='default@example.com', max_length=75),
                      keep_default=False)

        # Adding field 'EmailAddresses.primary'
        db.add_column('contacts_emailaddresses', 'primary',
                      self.gf('django.db.models.fields.EmailField')(default='default@example.com', max_length=75),
                      keep_default=False)

        # Deleting field 'EmailAddresses.type'
        db.delete_column('contacts_emailaddresses', 'type')

        # Deleting field 'EmailAddresses.contact'
        db.delete_column('contacts_emailaddresses', 'contact_id')

        # Deleting field 'EmailAddresses.email'
        db.delete_column('contacts_emailaddresses', 'email')

        # Deleting field 'PhoneNumber.contact'
        db.delete_column('contacts_phonenumber', 'contact_id')

        # Adding field 'Person.emails'
        db.add_column('contacts_person', 'emails',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['contacts.EmailAddresses']),
                      keep_default=False)

        # Deleting field 'Person.on_phone'
        db.delete_column('contacts_person', 'on_phone')


    models = {
        'contacts.emailaddresses': {
            'Meta': {'object_name': 'EmailAddresses'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Person']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'contacts.event': {
            'Meta': {'object_name': 'Event'},
            'attendees': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts.Person']", 'symmetrical': 'False'}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'contacts.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'persons': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contacts.Person']", 'symmetrical': 'False'})
        },
        'contacts.person': {
            'Meta': {'object_name': 'Person'},
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'first': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lkdin_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nick_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'on_phone': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'contacts.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Person']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['contacts']