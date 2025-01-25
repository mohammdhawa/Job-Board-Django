from django.shortcuts import render, redirect
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    
    if request.method == 'POST':
        form  = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def profile(request):
    profile = Profile.objects.get(user=request.user)
    
    context = {'profile': profile}
    return render(request, 'accounts/profile.html', context)

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    
    context = {'userform': userform, 'profileform': profileform}
    return render(request, 'accounts/profile_edit.html', context)

def profile_delete(request):
    pass
