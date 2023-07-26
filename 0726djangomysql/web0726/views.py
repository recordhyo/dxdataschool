from django.shortcuts import render
from django.http import HttpResponse
from web0726.models import product
# Create your views here.

# 요청 처리하는 함수의 매개변수는 request
# request 객체 안에는 클라이언트에 대한 정보가 저장되어 있음
def index(request) :
    return HttpResponse("<h1>Hi django</h1>")
def display(request) :
    return render(request, "display.html")

def template(request) :
    age = 28
    data = ["Stack", "Queue", "Deque","LinkedLIst", "Tree", "Graph", "Array"]
    # HTML 데이터 전송하고자하면 세번째 변수에 Dict 만들어서 데이터 이름과 데이터 기재
    return render(request, "template.html", {"age":age, "data":data})

def fruits(request) :
    data = product.objects.all()
    return render(request, "fruits.html", {"data":data})


def detail(request, itemid) :
    item = product.objects.get(itemid = itemid)
    return render(request, 'detail.html', {'item':item})