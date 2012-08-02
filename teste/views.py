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
    if request.GET:
        login = Login(request.GET)
        if login.is_valid():
            if login.clean["username"] == "adriano" and login.clean["password"] == "1234":
                return jrender({"status":"ok", "token":"654321"})

    return jrender({"status":"invalid"})

#@csrf_exempt
def pessoa(request, token):
    pass

