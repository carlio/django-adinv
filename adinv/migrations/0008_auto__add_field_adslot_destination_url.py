# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AdSlot.destination_url'
        db.add_column('adinv_adslot', 'destination_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AdSlot.destination_url'
        db.delete_column('adinv_adslot', 'destination_url')


    models = {
        'adinv.adslot': {
            'Meta': {'object_name': 'AdSlot'},
            'ad_chooser': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'destination_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
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
            'impression': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adinv.Impression']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
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