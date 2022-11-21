from django.shortcuts import render

def signin(request):
    return render(request, 'accounts/signin.html')

def signup(request):
    return render(request, 'accounts/signup.html')

def profile(request):
    return render(request, 'accounts/profile.html')
