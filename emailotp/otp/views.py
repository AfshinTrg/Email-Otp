from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterEmailForm, VerifyCodeForm
from django.contrib import messages
import random
from .utils import send_otp_code
from .models import OtpCode
from decouple import config
from datetime import datetime, timedelta


class HomeView(View):

    def get(self, request):
        return render(request, 'otp/home.html')


class RegisterEmail(View):
    def get(self, request):
        form = RegisterEmailForm
        return render(request, 'otp/register_email.html', {'form': form})

    def post(self, request):
        form = RegisterEmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            random_code = random.randint(1000, 9999)
            OtpCode.objects.create(email=cd['email'], code=random_code)
            send_otp_code(cd['email'], random_code)
            request.session['email_info'] = {
                'email': cd['email'],
            }
            messages.success(request, 'we sent you a code(email)', 'success')
            return redirect('otp:verify_code')


class VerifyCode(View):
    def get(self, request):
        form = VerifyCodeForm
        return render(request, 'otp/verify_code.html', {'form': form})

    def post(self, request):
        user_session = request.session['email_info']
        code_instance = OtpCode.objects.get(email=user_session['email'])
        expired_time = code_instance.created + timedelta(minutes=1)
        print('=' * 90)
        print(expired_time)
        if expired_time > datetime.now():
            form = VerifyCodeForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                if cd['code'] == code_instance.code:
                    messages.success(request, 'Your code is correct', 'success')
                    code_instance.delete()
                    return redirect('otp:home')
                else:
                    messages.error(request, 'this code is wrong', 'danger')
                    return redirect('otp:verify_code')
        else:
            code_instance.delete()
            messages.error(request, 'Your time expired, please try again', 'danger')
            return redirect('otp:register_email')
