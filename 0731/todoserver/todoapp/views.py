import json
import datetime
from django.shortcuts import render
from django.views import View #응답하는 클래스
from .models import ToDo
from django.http import JsonResponse #json 응답을만들기 위한 import
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


#클래스의 get, post, put, delete 메서드가 각 요청 방식을 처리
@method_decorator(csrf_exempt, name='dispatch')
class TodoView(View) :
    #GET 요청 처리
    def get(self, request):
        # 파라미터 읽어오기 - userid 없으면 None
        userid = request.GET.get("userid", None)
        #userid에 해당하는 데이터 todos에 불러오기
        if userid != None :
            todos = ToDo.objects.filter(userid = userid)
        else :
            todos = ToDo.objects.all()
        #Json 응답 list라는 키로 검색된 데이터를 list로 전달
        return JsonResponse({'list':list(todos.values())},status=status.HTTP_200_OK)
    #POST 요청 처리
    def post(self, request):
        # 파라미터 읽기
        params = json.loads(request.body)
        userid = params["userid"]
        title = params["title"]

        #삽입할 객체 생성
        todo = ToDo()
        todo.userid = userid
        todo.title = title
        todo.done = False
        todo.moddate = datetime.datetime.today()

        #데이터 삽입
        todo.save()

        #삽입 후 결과 처리
        #일반적으로 삽입 한 데이터만 리턴하거나 전체 데이터 리턴
        todos = ToDo.objects.filter(userid=userid)
        return JsonResponse({'list': list(todos.values())}, status=status.HTTP_200_OK)

    def put(self,request):
        #클라이언트의 파라미터 읽기
        params = json.loads(request.body)
        id = params["id"]
        userid = params["userid"]
        done = params["done"]

        #서버에서의 처리
        #여기서 데이터베이스 작업 이외 작업 하면 별도의 클래스 만들어서 처리한 후 리턴받아서 작업 수행
        #id에 해당하는 데이터 찾아서 done의 값을 수정하는 것
        todo = ToDo.objects.get(id = id)
        todo.done = done
        todo.save()
        #응답 만들기
        todos = ToDo.objects.filter(userid=userid)
        return JsonResponse({'list': list(todos.values())}, status=status.HTTP_200_OK)

    def delete(self,request):
        #파라미터 읽기
        params = json.loads(request.body)
        id = params["id"]
        userid = params["userid"]

        #데이터 가져오기
        todo = ToDo.objects.get(id=id)

        #데이터 삭제
        todo.delete()

        # 응답 만들기
        todos = ToDo.objects.filter(userid=userid)
        return JsonResponse({'list': list(todos.values())}, status=status.HTTP_200_OK)
