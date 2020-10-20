from django.shortcuts import render
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from django.db import connection
from .models import *

@csrf_exempt
def index(request):
    return HttpResponse("Main page words. "+str(datetime.datetime.now()))


@csrf_exempt
def update_Word(request):
    if request.method == 'POST':
        res=Word.uploadJson(request.body.decode())
        if res=="":
            return HttpResponse("All good. |"+str(datetime.datetime.now()))   
        return HttpResponse(res+" |"+str(datetime.datetime.now()),status=404)  
    
    return HttpResponse("Only post requests. "+str(datetime.datetime.now()),status=404)
    #return render(request, 'form.html', {'form': form})