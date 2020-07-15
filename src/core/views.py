from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
# Create your views here.


@login_required
def home(request):
    context = {
        'title': 'home',
    }
    return render(request, 'core/home.html', context)

def splash(request):

    context = {
        'title': 'splash',
    }
    return render(request, 'core/splash.html', context)

@login_required
def about(request):

    context = {
        'title': 'About',
    }
    return render(request, 'core/about.html', context)


@login_required
def suggestions(request):

    context = {
        'title': 'Suggestions',
    }
    return render(request, 'core/suggestions.html', context)


@login_required
def forum(request):

    context = {
        'title': 'Discussion Forum',
    }
    return render(request, 'core/forum.html', context)


