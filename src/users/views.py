from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ChoicesForm,JuniorRegisterForm, ProfileUpdateForm, UserUpdateForm,SeniorRegisterForm,TeacherRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = ChoicesForm(request.POST)
        if form.is_valid():
            if(form.cleaned_data.get('register_as')=='0'):
                return redirect('junior')
            elif(form.cleaned_data.get('register_as')=='1'):
                return redirect('senior')
            else:
                return redirect('teacher')
    else:
        form = ChoicesForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

def junior(request):
    if request.method == 'POST':
        form = JuniorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created Now you can Log In !!')
            return redirect('login')
            
    else:
        form = JuniorRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/junior.html', context)

def senior(request):
    if request.method == 'POST':
        form = SeniorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created Now you can Log In !!')
            return redirect('login')
    else:
        form = SeniorRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/senior.html', context)

def teacher(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created Now you can Log In !!')
            return redirect('login')
    else:
        form = TeacherRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/teacher.html', context)



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Info is Updated!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
