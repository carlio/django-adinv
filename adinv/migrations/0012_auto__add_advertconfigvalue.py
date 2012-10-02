# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AdvertConfigValue'
        db.create_table('adinv_advertconfigvalue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('advert', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adinv.Advert'])),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('adinv', ['AdvertConfigValue'])


    def backwards(self, orm):
        # Deleting model 'AdvertConfigValue'
        db.delete_table('adinv_advertconfigvalue')


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
            'dimensions': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adinv.SlotDimensions']"}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'adinv.advertconfigvalue': {
            'Meta': {'object_name': 'AdvertConfigValue'},
            'advert': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adinv.Advert']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
        'adinv.jsadvert': {
            'Meta': {'object_name': 'JSAdvert', '_ormbases': ['adinv.Advert']},
            'advert_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['adinv.Advert']", 'unique': 'True', 'primary_key': 'True'}),
            'code': ('django.db.models.fields.TextField', [], {})
        },
        'adinv.simpleimageadvert': {
            'Meta': {'object_name': 'SimpleImageAdvert', '_ormbases': ['adinv.Advert']},
            'advert_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['adinv.Advert']", 'unique': 'True', 'primary_key': 'True'}),
            'destination_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'track_clicks': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
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