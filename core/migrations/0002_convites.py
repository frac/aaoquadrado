#coding:utf8
from south.db import db
from django.db import models
from aaoquadrado.core.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Convite'
        db.create_table('core_convite', (
            ('id', orm['core.convite:id']),
            ('nome', orm['core.convite:nome']),
            ('email', orm['core.convite:email']),
            ('convidados', orm['core.convite:convidados']),
            ('convites', orm['core.convite:convites']),
            ('dequem', orm['core.convite:dequem']),
            ('rspv', orm['core.convite:rspv']),
            ('adultos', orm['core.convite:adultos']),
            ('criancas', orm['core.convite:criancas']),
        ))
        db.send_create_signal('core', ['Convite'])
    
    def backwards(self, orm):
        
        # Deleting model 'Convite'
        db.delete_table('core_convite')
        
    
    
    models = {
        'core.convite': {
            'adultos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'convidados': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'convites': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'criancas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dequem': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75','null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '256','null': 'True', 'blank': 'True'}),
            'rspv': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['core']
