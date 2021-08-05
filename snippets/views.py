from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest


def top(request):
    return HttpResponse(b"Hello World")
def snippet_new(request):
    return HttpResponse('スニペットの登録')
def snippet_edit(request):
    return HttpResponse('スニペットの編集')
def snippet_detail(request,snippet_id):
    return HttpResponse('スニペットの詳細閲覧')




# Create your views here.
