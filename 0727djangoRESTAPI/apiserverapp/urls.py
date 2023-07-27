from django.urls import path
from .views import helloAPI, booksAPI, bookAPI

urlpatterns = [
    # example/hello 요청이 오면 helloAPI 함수가 처리
    path("hello/", helloAPI),
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/",bookAPI)
]
