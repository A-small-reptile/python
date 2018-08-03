from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.views.generic.base import View

from users.models import UserProfile,EmailVerifyRecord
from users.forms import LoginForm,RegisterForm,ForgetPasswdForm,ResetPasswdForm

from utils.email_send import send_register_email

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class ActiveView(View):
    def get(self,request,active_code):
        records_code=EmailVerifyRecord.objects.filter(code=active_code)
        if records_code:
            for record in records_code:
                email=record.email
                user=UserProfile.objects.filter(email=email)
                if not user:
                    user.is_active = True
                    user.save()
                    return render(request, 'login.html', {})
                else:
                    msg='用户已存在,请重新注册'
                    return  redirect('/register/')
        else:
            return  render(request,'active_code.html',{})


class RegisterView(View):
    def get(self,request):
        register_form=RegisterForm()
        return render(request,'register.html',{'register_form':register_form})
    def post(self,request):
        register_form=RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username', "")
            if UserProfile.objects.filter(username=user_name):
                return render(request,'register.html',{})
            else:
                pass_word = request.POST.get('password', "")
                email=request.POST.get('email',"")
                user_profile=UserProfile()
                user_profile.is_active=False
                user_profile.username=user_name
                user_profile.email=email
                user_profile.password=make_password(pass_word)
                user_profile.save()
                send_register_email(email, 'register')
                return render(request,'login.html',{})
        else:
            return render(request,'register.html',{})

class LoginView(View):
    def get(self,request):
        return render(request, 'login.html', {})
    def post(self,request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', "")
            pass_word = request.POST.get('password', "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html', {})
                else:
                    return render(request,'login.html',{})
            else:
                msg = u'用户名或是密码错误'
                return render(request, 'login.html', {})
        else:
            return render(request, 'login.html', {})

class ForgetPasswdView(View):
    def get(self,request):
        forget_form = ForgetPasswdForm()
        return render(request,'forget_passwd.html',{'forget_form':forget_form})
    def post(self,request):
        forget_user=ForgetPasswdForm(request.POST)
        if forget_user.is_valid():
            email=request.POST.get('email','')
            if UserProfile.objects.get(email=email):
                send_register_email(email,send_type='forget',)
                return render(request,'send_success.html')
            else:
                msg_error='用户不存在'
                return redirect('/forget/')
        else:
            msg_error='输入的邮箱或验证码错误'
            return redirect('/forget/')

class ResetView(View):
    def get(self,request,active_code):
        records_code=EmailVerifyRecord.objects.filter(code=active_code)
        if records_code:
            for record in records_code:
                email=record.email
                return render(request, 'reset_passwd.html', {'email':email})
        else:
            return  render(request,'active_code.html',{})

class ModifyPwdView(View):
    def post(self,request):
        modify_passwd=ResetPasswdForm(request.POST)
        if modify_passwd.is_valid():
            pwd1=request.POST.get('password','')
            pwd2=request.POST.get('password1','')
            email=request.POST.get('email','')
            if pwd1 != pwd2:
                return render(request, 'reset_passwd.html', {'email': email,'msg':'密码不一致'})
            user=UserProfile.objects.get(email=email)
            user.password=make_password(pwd1)
            user.save()
            return redirect('/login/')
        else:
            email = request.POST.get('email', '')
            return render(request, 'reset_passwd.html', {'email': email,})


