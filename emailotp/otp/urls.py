from django.urls import path
from . import views

app_name = 'otp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

]
