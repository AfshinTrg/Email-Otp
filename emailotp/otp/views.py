from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterEmailForm
from django.contrib import messages
import random
from .utils import send_otp_code
from .models import OtpCode
from decouple import config


class HomeView(View):

    def get(self, request):
        return render(request, 'otp/home.html')


class RegisterEmail(View):
    def get(self, request):
        form = RegisterEmailForm
        return render(request, config('next'), {'form': form})

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
            return redirect('otp:home')


