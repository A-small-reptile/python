from django import forms

#表单验证
class UserFromsHanlder(forms.Form):
    user_name=forms.CharField(max_length=10)
    password1=forms.CharField(max_length=16)
    passeord2=forms.CharField(max_length=16)
    user_email=forms.EmailField(max_length=50)

    """"#检查用户名是否重复
    def clean_user_name(self):
        ret=UserDetail.objects.filter(user_name=self.cleaned_data.get('user_name'))
        if not ret:
            return self.cleaned_data.get('user_name')
        else:
            raise ValueError('用户已注册')
    #密码是否全是数字
    def clean_user_password(self):
        data=self.cleaned_data.get('user_password1')
        if not data.isdigit():
            return self.cleaned_data.get('user_password1')
        else:
            raise ValueError('密码不能全是数字')

    def clean(self):
        if self.cleaned_data.get('user_password1')==self.cleaned_data.get('user_password2'):
            return self.cleaned_data

        else:
            raise ValueError('两次密码不一样')"""

