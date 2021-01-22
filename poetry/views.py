from django.shortcuts import render

from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from poetry.models import Love,Spiritual,Anger,Death,Family,Famous,Friendship,Holiday,Life,Nature,Sad,Christian,Coronavirus



# Create your views here.

# @login_required(login_url='/login/')
def index(request):
    return render(request, 'poetry/index.html')


@login_required(login_url='/login/')
def lovePoems(request):
    
    lovePoems=Love.objects.all()
    lovePoems=lovePoems[::-1]

    context={  
        'lovePoems':lovePoems, 
    }
    return render(request,'poetry/lovePoems.html', context)

