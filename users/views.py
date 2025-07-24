from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationFrom

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Acount was created for {username}!")
            return redirect('login')
    else:
            form=UserRegistrationFrom()
    return render(request,'users/register.html',{"form":form})
    
@login_required
def profile(request):
    return render(request,'users/profile.html')
