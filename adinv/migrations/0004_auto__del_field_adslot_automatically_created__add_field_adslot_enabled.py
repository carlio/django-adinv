# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'AdSlot.automatically_created'
        db.delete_column('adinv_adslot', 'automatically_created')

        # Adding field 'AdSlot.enabled'
        db.add_column('adinv_adslot', 'enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'AdSlot.dimensions'
        db.alter_column('adinv_adslot', 'dimensions_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adinv.SlotDimensions'], null=True))

    def backwards(self, orm):
        # Adding field 'AdSlot.automatically_created'
        db.add_column('adinv_adslot', 'automatically_created',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'AdSlot.enabled'
        db.delete_column('adinv_adslot', 'enabled')


        # User chose to not deal with backwards NULL issues for 'AdSlot.dimensions'
        raise RuntimeError("Cannot reverse this migration. 'AdSlot.dimensions' and its values cannot be restored.")

    models = {
        'adinv.adslot': {
            'Meta': {'object_name': 'AdSlot'},
            'dimensions': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adinv.SlotDimensions']", 'null': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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