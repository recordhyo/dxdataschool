from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request) :
    # HTML을 직접 작성해서 출력
    # return HttpResponse("<H1>Hello Django</H1>")

    # HTML 파일을 출력
    return render(request, 'index.html')

def hello(request) :
    return HttpResponse("<h3>Hello</h3>")