from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
from django.views.generic.list import View
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


@login_required(login_url='/accounts/login/')
def contact_post(request):
    if request.method == "POST":
        contact_name = request.POST['contact_name']
        contact_yearold = request.POST['contact_yearold']
        contact_sex = request.POST['contact_sex']
        contact_email = request.POST['contact_email']
        contact_phone = request.POST['contact_phone']
        contact_time = request.POST['contact_time']
        contact_subject = request.POST['contact_subject']
        message = request.POST['message']

        send_mail(
            'Đặt lịch thành công tại phòng khám XYZ',
            'Xin chào:' +' '+contact_name+',' +
            '\n\nSĐT:'+ ' '+contact_phone+',' +
            '\n\nThời gian khám:'+' '+contact_time+','+
            '\n\nVấn đề:'+ ' '+ contact_subject+','+
            '\n\nVui lòng đợi nhân viên xác nhận lần 2 qua sđt đã đăng ký,'
            '\n\nPhòng khám XYZ chân thành cảm ơn vì đã tin tưởng dịch vụ của chúng tôi,'
            '\n\nCảm ơn.',
            contact_email,
            [contact_email],
            fail_silently = False,

        )

        return render(request, 'contact/contact.html', {'contact_name': contact_name})
    else:
        return render(request, 'contact/contact.html', {})