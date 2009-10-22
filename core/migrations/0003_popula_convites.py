#coding:utf8
from south.db import db
from django.db import models
from aaoquadrado.core.models import *

class Migration:
    
    def forwards(self, orm):
        
        CONVIDADOS = (        
            (1,"neide",1),
            (1,"ennio",0),
            (1,"vovo'",0),
            (1,"fernando",1),
            (1,"ivan",0),
            (1,"bia",1),
            (1,"juju",1),
            (1,"vicente",0),
            (4,"raoul",1),
            (1,"maio",1),
            (1,"peter",0),
            (1,"michele",1),
            (4,"jennifer",1),
            (4,"bas",1),
            (1,"elias",1),
            (1,"nene",0),
            (2,"zeca",1),
            (2,"camila",1),
            (2,"paulo",1),
            (2,"luiz",1),
            (2,"monica",0),
            (1,"drica",0),
            (2,"carlos",1),
            (1,"maria beatriz",0),
            (1,"fer",1),
            (2,"carolina",1),
            (1,"Joao Pedro",1),
            (2,"madu",1),
            (1,"Julia",0),
            (1,"debora",1),
            (1,"tiago",1),
            (1,"neusa",1),
            (2,"eduardo dias",1),
            (3,"bia stucchi",1),
            (2,"tamas",1),
            (2,"rita",1),
            (2,"heleninha",1),
            (2,"tia cristina",1),
            (2,"Silvinha + Luiz",1),
            (2,"Alda + Teofilo",1),
            (3,"Ivone + Regis",1),
            (1,"Renata",1),
            (1,"Lucia Cavalcanti",1),
            (2,"Fleury e Ivanira",1),
            (2,"Ivan ( tico) e filha",1),
            (2,"Bia e Junior",1),
            (2,"Zeze e Briganti",1),
            (2,"Miguel e Familia",1),
            (1,"Marcia e irmã",1),
            (1,"Shoko / Sa e filho",1),
            (2,"Sonia e marido",1),
            (1,"lidia",1),
            (2,"rita",1),
            (2,"isabel",1),
            (1,"sizinha",1),
            (1,"kai",0),
            (2,"Ric",0),
            (2,"Fabio",1),
            (1,"carlos alves",1),
            (2,"maurao",1),
            (2,"rbp",1),
            (2,"leo",1),
            (2,"luciano ramalho",1),
            (2,"erico",1),
            (2,"caffo",1),
            (3,"hb",1),
            (1,"paulo moretto",1),
            (2,"bibi andre",1),
            (2,"chambs",1),
            (2,"chf",1),
            (2,"livio e gustavo",1),
            (1,"isabela",1),
            (2,"dayan",1),
            (1,"rafa",1),
            (2,"liv",1),
            (3,"karina",1),
            (2,"bru ge",1),
            (1,"lu lobo",1),
            (2,"andy",1),
            (2.5,"ju fukuda",1),
            (2,"dani wagner",1),
            (1,"namica",1),
            (2,"lincoln",1),
            (2,"fabi mirella",1),
            (1,"ana maria",1),
            (2,"mari stucchi",1),
            (2,"stephanie",1),
            (2,"ann marie",1),
            (1,"Kuba",1),
            (1,"tati nolla",1),
            (2,"carol martins",1),
            (1,"carol morgante",1),
            (2,"glin",1),
            (2,"lagosta",1),
            (2,"bianchi",1),
            (1,"mercedes",1),
            (2,"moki",1),
            (2,"nicia dudu",1),
            (1,"piccino",1),
            (1,"re faria",1),
            (2,"lauretta",1),
            (2.5,"carol seixas",1),
            (2,"paula asprino",1),
            (2,"lego",1),
            (1,"lauw",1),
            (3,"Luis",1),
            (2,"Gi",1),
            (2,"Bruno",1),
            (1,"Tati",1),
            (1,"Eduardo",1),
            (1,"Marcela",1),
            (2,"Karen",1),
            
        )

    
        for conv in CONVIDADOS:
            con = Convite()
            con.convidados = conv[0]
            con.nome = conv[1]
            con.convites = conv[2]
            con.save()
        




    
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
