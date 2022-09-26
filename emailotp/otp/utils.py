from django.conf import settings
from django.core.mail import send_mail


def send_otp_code(email, code):
    subject = 'Thank you for registering to our site'
    message = f'Thank you for registering to our site, Your code is : {code}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)
