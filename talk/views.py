from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone

from talk.models import Post


def index(request):
    # 리스트 출력
    postList = Post.objects.order_by('-date')
    context = {
        'postList' : postList
    }
    return render(request, 'talk/list.html', context)

def detail(request, postId):
    # 상세 보기
    post = Post.objects.get(id=postId)
    context = {
        'post' : post
    }
    return render(request, 'talk/detail.html', context)

def answer_create(request, postId):
    # 답글 추가
    post = get_object_or_404(Post, pk=postId)
    post.answer_set.create(content = request.POST.get('content'), date=timezone.now())
    return redirect('talk:detail', postId=postId)
