# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('contacts_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fb_id', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('first', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lkdin_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nick_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('emails', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.EmailAddresses'])),
        ))
        db.send_create_signal('contacts', ['Person'])

        # Adding model 'Group'
        db.create_table('contacts_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('contacts', ['Group'])

        # Adding M2M table for field persons on 'Group'
        db.create_table('contacts_group_persons', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['contacts.group'], null=False)),
            ('person', models.ForeignKey(orm['contacts.person'], null=False))
        ))
        db.create_unique('contacts_group_persons', ['group_id', 'person_id'])

        # Adding model 'Event'
        db.create_table('contacts_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('contacts', ['Event'])

        # Adding M2M table for field attendees on 'Event'
        db.create_table('contacts_event_attendees', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['contacts.event'], null=False)),
            ('person', models.ForeignKey(orm['contacts.person'], null=False))
        ))
        db.create_unique('contacts_event_attendees', ['event_id', 'person_id'])

        # Adding M2M table for field groups on 'Event'
        db.create_table('contacts_event_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['contacts.event'], null=False)),
            ('group', models.ForeignKey(orm['contacts.group'], null=False))
        ))
        db.create_unique('contacts_event_groups', ['event_id', 'group_id'])

        # Adding model 'EmailAddresses'
        db.create_table('contacts_emailaddresses', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('primary', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('secondary', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('ternary', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('contacts', ['EmailAddresses'])

        # Adding model 'PhoneNumber'
        db.create_table('contacts_phonenumber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('phone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20)),
        ))
        db.send_create_signal('contacts', ['PhoneNumber'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('contacts_person')

        # Deleting model 'Group'
        db.delete_table('contacts_group')

        # Removing M2M table for field persons on 'Group'
        db.delete_table('contacts_group_persons')

        # Deleting model 'Event'
        db.delete_table('contacts_event')

        # Removing M2M table for field attendees on 'Event'
        db.delete_table('contacts_event_attendees')

        # Removing M2M table for field groups on 'Event'
        db.delete_table('contacts_event_groups')

        # Deleting model 'EmailAddresses'
        db.delete_table('contacts_emailaddresses')

        # Deleting model 'PhoneNumber'
        db.delete_table('contacts_phonenumber')


    models = {
        'contacts.emailaddresses': {
            'Meta': {'object_name': 'EmailAddresses'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'secondary': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'ternary': ('django.db.models.fields.EmailField', [], {'max_length': '75'})
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
            'emails': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.EmailAddresses']"}),
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'first': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lkdin_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nick_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'contacts.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['contacts']