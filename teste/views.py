from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django import forms
import json
from django.core.serializers.json import DjangoJSONEncoder


def jrender(context):
    response = HttpResponse(json.dumps(context, cls=DjangoJSONEncoder), 'application/json')
    response["Access-Control-Allow-Origin"] = "*"
    return response


class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


#@csrf_exempt
def login(request):
    if request.POST:
        login = Login(request.POST)
        if login.is_valid():
            if login.cleaned_data["username"] == "1234" and login.cleaned_data["password"] == "adriano":
                return jrender({"status":"ok", "token":"654321"})

    return jrender({"status":"invalid"})
import datetime

#@csrf_exempt
def pessoa(request, token):
    if token == "654321":
        pessoa = { 'base_id': 8255,
             'base_impresso_id': None,
             'boleto_individual': False,
             'dt': datetime.date(2009, 3, 7),
             'dt_falecimento': None,
             'dt_nasc': datetime.date(1982, 11, 3),
             'email': u'fhendo@gmail.com',
             'escolaridade': u'superior',
             'estado_civil': u'solteiro',
             'familia_id': 10,
             'grupo_profissional_id': None,
             'id': 29,
             'lembrete_senha': u'Oi',
             'nacionalidade_id': 6,
             'nome': u'F\xe1bio Hideki Endo',
             'nome_busca': u'fabio hideki endo',
             'profissao': u'',
             'sexo': u'm',
             'timestamp': datetime.datetime(2011, 10, 27, 11, 51, 7, 435640),
             'user_id': 4960}

        return jrender({"status":"ok", "pessoa":pessoa})
    
    return jrender({"status":"invalid"})

