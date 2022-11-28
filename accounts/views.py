from django.shortcuts import render, redirect
from django.contrib import messages

def signin(request):
    if request.method == 'POST' and 'btnsignin' in request.POST:
        messages.info(request, 'hello')
        return redirect('accounts:signin')
    else:
        return render(request, 'accounts/signin.html')

def signup(request):
    if request.method == 'POST' and 'btnsignup' in request.POST:
        messages.info(request, 'hello')
        return redirect('accounts:signup')
    else:
        return render(request, 'accounts/signup.html')

def profile(request):
    if request.method == 'POST' and 'btnprofile' in request.POST:
        messages.info(request, 'hello')
        return redirect('accounts:profile')
    else:
        return render(request, 'accounts/profile.html')
