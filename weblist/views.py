from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import WebList

# Create your views here.


def nav(request):
    web_list = WebList.objects.all()
    is_auth = request.user.is_authenticated
    # if request.user.is_authenticated:
    #     is_auth = True
    # else:
    #     is_auth = False
    print(is_auth)
    return render(request, 'home.html', {'alist': [1, 2, 3, 4], 'web_list': web_list, 'is_auth': is_auth})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 与数据库中的用户名和密码比对，django默认保存密码是以哈希形式存储，并不是明文密码，这里的password验证默认调用的是User类的check_password方法，以哈希值比较。
        user = authenticate(request, username=username, password=password)
        # 验证如果用户不为空
        if user is not None:
            # login方法登录
            login(request, user)
            # 返回登录成功信息

    return HttpResponseRedirect('/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
