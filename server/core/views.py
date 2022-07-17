from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest,\
                        HttpResponseForbidden, HttpResponseNotFound,\
                        FileResponse
from django.views.decorators.http import require_http_methods

from core.models import *
import time
import json
import os
from apollo.settings import BASE_DIR
CLIENT_MIN_BALANCE = 0
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def task1_form(request):
    json_str=((request.body).decode('utf-8'))
    json_obj=json.loads(json_str)
    print(json_obj)
    answer = {"validation_score": 5}
    return HttpResponse( answer)


def task2_form(request):
    json_str=((request.body).decode('utf-8'))
    json_obj=json.loads(json_str)
    print(json_obj)
    answer =  {
        "tnved": "",
        "reglament": "",
        "group": "",
        'productName': ""
      },
    return HttpResponse( answer)



def index_page(request):
    return FileResponse(open(os.path.join(BASE_DIR,
                                          r"static/index.html"),
                             'rb'))


def favicon(request):
    return FileResponse(open(os.path.join(BASE_DIR,
                                          r"static/favicon.ico"),
                             'rb'))


def static_delivery(request, path=""):
    print(f"serve static {path}")
    if os.path.isfile(os.path.join(BASE_DIR, 'static/', path)):
        response = FileResponse(open(os.path.join(BASE_DIR,
                                     'static/',
                                     path), 'rb'))
        if 'css'in path:
            response['Content-Type'] = 'text/css'
        if 'js' in path:
            response['Content-Type'] = 'text/javascript'

    else:
        response = HttpResponseNotFound()
    return response


