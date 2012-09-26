# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'AdDimensions'
        db.delete_table('adinv_addimensions')

        # Adding model 'SlotDimensions'
        db.create_table('adinv_slotdimensions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('width', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('height', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('adinv', ['SlotDimensions'])


        # Changing field 'AdSlot.dimensions'
        db.alter_column('adinv_adslot', 'dimensions_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adinv.SlotDimensions']))

    def backwards(self, orm):
        # Adding model 'AdDimensions'
        db.create_table('adinv_addimensions', (
            ('width', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('height', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('adinv', ['AdDimensions'])

        # Deleting model 'SlotDimensions'
        db.delete_table('adinv_slotdimensions')


        # Changing field 'AdSlot.dimensions'
        db.alter_column('adinv_adslot', 'dimensions_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adinv.AdDimensions']))

    models = {
        'adinv.adslot': {
            'Meta': {'object_name': 'AdSlot'},
            'dimensions': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adinv.SlotDimensions']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'adinv.slotdimensions': {
            'Meta': {'object_name': 'SlotDimensions'},
            'height': ('django.db.models.fields.SmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'width': ('django.db.models.fields.SmallIntegerField', [], {})
        }
    }

    complete_apps = ['adinv']