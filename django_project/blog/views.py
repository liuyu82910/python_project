from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'blog/home.html')


def about(request):
    return render(request,'blog/about.html')


def method_splitter(request, GET=None, POST=None):
    if request.method == 'GET' and GET is not None:
        return GET(request)
    elif request.method == 'POST' and POST is not None:
        return POST(request)
    raise Http404

def some_page_get(request):
    assert request.method == 'GET'
    return render(request, 'test.html')

def some_page_post(request):
    assert request.method == 'POST'
    return HttpResponseRedirect('/yello/')