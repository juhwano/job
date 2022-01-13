from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm

def index(request):
    return HttpResponse('<h1>프로젝트 메인 테스트</h1><br/>'
                        '<a href="index">홈페이지 메인</a><br/>'
                        '<a href="talk">직업 게시판</a><br/>'
                        '<a href="users">회원 관리</a><br/>'
                        '<a href="discover">직업 탐색</a><br/>'
                        '<a href="admin">관리자 페이지</a><br/>'
                        )