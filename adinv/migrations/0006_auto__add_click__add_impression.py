# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Click'
        db.create_table('adinv_click', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('impression', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adinv.Impression'])),
        ))
        db.send_create_signal('adinv', ['Click'])

        # Adding model 'Impression'
        db.create_table('adinv_impression', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('advert', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adinv.Advert'])),
            ('adslot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adinv.AdSlot'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('adinv', ['Impression'])


    def backwards(self, orm):
        # Deleting model 'Click'
        db.delete_table('adinv_click')

        # Deleting model 'Impression'
        db.delete_table('adinv_impression')


    models = {
        'adinv.adslot': {
            'Meta': {'object_name': 'AdSlot'},
            'ad_chooser': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dimensions': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adinv.SlotDimensions']", 'null': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'adinv.advert': {
            'Meta': {'object_name': 'Advert'},
            'code': ('django.db.models.fields.TextField', [], {}),
            'dimensions': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adinv.SlotDimensions']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'adinv.click': {
            'Meta': {'object_name': 'Click'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impression': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adinv.Impression']"})
        },
        'adinv.impression': {
            'Meta': {'object_name': 'Impression'},
            'adslot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adinv.AdSlot']"}),
            'advert': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adinv.Advert']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
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