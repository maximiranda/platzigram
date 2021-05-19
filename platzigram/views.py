"""platzigram views."""

from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now()
    print(request.GET)
    return HttpResponse(f"oh, hi current server time is {str(now)}")


def ordenada(request):
    n = request.GET["n"].split(",")
    sorted_list=sorted(n)
    return HttpResponse(sorted_list)