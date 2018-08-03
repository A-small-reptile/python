#_*_ encoding:utf-8 _*_
from random import Random

from django.core.mail import send_mail
from django.conf import settings

from users.models import EmailVerifyRecord

def random_str(randomlength=8):
    str=''
    char='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length=len(char)-1
    random=Random()
    for i in range(randomlength):
        str +=char[random.randint(0,length)]
    return str

def send_register_email(email,send_type='register',):
    email_record=EmailVerifyRecord()
    code=random_str(randomlength=16)
    email_record.code=code
    email_record.email=email
    email_record.send_type=send_type
    email_record.save()
    to_email=email

    if send_type=='register':
        email_title=u'平凡,致简博客注册激活'
        email_content=u'请点击下方链接进行激活：http:127.0.0.1:8000/active/{0}'.format(code)

        send_mail(email_title,email_content,settings.DEFAULT_FROM_EMAIL,[email])

    elif send_type=='forget':
        email_title=u'平凡,致简博客用户密码重置'
        email_content = u'请点击下方链接进行进行密码重置：http:127.0.0.1:8000/reset/{0}'.format(code)

        send_mail(email_title,email_content,settings.DEFAULT_FROM_EMAIL,[email])









