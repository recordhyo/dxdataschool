#render : 화면에 그리는 것
#redirect : 현재까지의 흐름을 끊고 새로운 요청을 생성, redirect 는 작업이 완료되었다는 의미
#redirect 와 forwarding 의 가장 큰 차이점은 새로고침
#forwarding 은 새로고침을 하면 작업을 다시하고 redirect 는 새로고치믕ㄹ 하면 화면만 다시 출력
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import FileUpload
import uuid

#데이터베이스의 모든 내용을 가져와서 뷰로 보내는 함수


def fileUpload(request):
    #전송 방식을 확인
    if request.method == 'POST':
        #파라미터가 있으면 파라미터를 읽기
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES.get("imgfile")

        #확장자와 파일 이름 사이 uuid 추가
        idx = img.name.rfind(".")
        if idx != -1 :
            img.name = img.name[:idx] + str(uuid.uuid4()) + img.name[idx:]
        else :
            img.name = img.name + str(uuid.uuid4())
        #유효성검사를 수행한 후 필요한 model을 생성
        fileupload = FileUpload(
            title=title,
            content=content,
            imgfile=img,
        )

        #작업을 수행
        fileupload.save()
        #결과를 리턴
        return redirect('fileupload')
    else:
        #데이터 생성
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        #출력할 뷰와 데이터를 하나로 묶어서 넘김
        return render(request, 'fileupload.html', context)