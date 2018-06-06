from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt




#其他的情况
def get_about(request):
    return render(request,'base/about.html')

def get_contact(request):
    return render(request,'base/contact.html')

def login_page(request):
    return render(request,'base/login.html')

def register_page(request):
    return render(request,'base/register.html')


#登录验证
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('user_name')
        password=request.POST.get('password')
        print('content:',request.POST)
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            print('登录成功')
            return redirect('/blog/',)
        else:
            print('用户不存在')
            return redirect('/login/')
    else:
        print('请求存在问题')
        return redirect('/login/')
#登出
def logout_view(request):
    logout(request)
    #需要添加内容
    return render(request,'home.html')
#注册情况
@csrf_exempt
def register_view(request):
    if request.method=='POST':
        print('content:',request.POST)
        username=request.POST.get('account')
        password=request.POST.get('password')
        useremail=request.POST.get('email')
        user=authenticate(username=username,password=password)
        if user:
            print('用户存在')
            return redirect('/register/')
        user_create=User.objects.create_user(username,useremail,password)
        user_create.save()
        print('注册成功')
        login(request,user_create)
        print('登录成功')
        return redirect(request,'/blog/')
    else:
        return redirect('/register/')



