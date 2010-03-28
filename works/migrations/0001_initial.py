# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Work'
        db.create_table('works_work', (
            ('date', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('works', ['Work'])

        # Adding model 'MediaFile'
        db.create_table('works_mediafile', (
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('works', ['MediaFile'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Work'
        db.delete_table('works_work')

        # Deleting model 'MediaFile'
        db.delete_table('works_mediafile')
    
    
    models = {
        'works.mediafile': {
            'Meta': {'object_name': 'MediaFile'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
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
