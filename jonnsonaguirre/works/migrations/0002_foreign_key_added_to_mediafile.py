# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'MediaFile.work'
        db.add_column('works_mediafile', 'work', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['works.Work']), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'MediaFile.work'
        db.delete_column('works_mediafile', 'work_id')
    
    
    models = {
        'works.mediafile': {
            'Meta': {'object_name': 'MediaFile'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['works.Work']"})
        },
        'works.work': {
            'Meta': {'object_name': 'Work'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }
    
    complete_apps = ['works']
