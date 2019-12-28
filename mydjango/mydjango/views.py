from django.http import HttpResponse, Http404
from datetime import datetime as dt
from datetime import timedelta as td
# from django.template.loader import get_template
# from django.template import Context
from django.shortcuts import render_to_response
def hello(request):
    return HttpResponse("Hello world")


def current_time(request):
    now=dt.now()
    html="<html><body><h1 style='background-color: tomato; color:white'>It is now %s ^___^</h1></body></html>" \
         % now.strftime('%H:%M:%S, %B %d, %Y')
    return HttpResponse(html)

def time_difference(request, offset):
    try:
        offset= round(float(offset))
    except ValueError:
        raise Http404()
    timediff=dt.now()+td(hours=offset)
    # html="<html><body><h1 style='font-size:50px; color: blue;text-align:center; border: 2px solid tomato; " \
    #      "border-radius: 5px; width:1000px; height: 60px;'>" \
    #      "In %s hour(s), it will be %s </h1></body></html>" % (offset, timediff)
    return render_to_response('time_diff.html',{'timediff': timediff.strftime('%H:%M:%S, %B/%d/%Y'),'offset': offset})

def cur_datetime(reqeust):
    now=dt.now()
    return render_to_response('cur_datetime.html',{'currentdatetime': now.strftime('%H:%M:%S, %B %d, %Y')})





