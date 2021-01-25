from django.shortcuts import render

from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from poetry.models import Love,Spiritual,Anger,Death,Family,Famous,Friendship,Holiday,Life,Nature,Sad,Christian,Coronavirus
from poetry.forms import NewAngerForm,NewChristianForm,NewCoronavirusForm,NewDeathForm,NewFamilyForm,NewFamousForm,NewFriendshipForm,NewHolidayForm,NewLifeForm,NewLoveForm,NewNatureForm,NewSadForm,NewSpiritualForm


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

@login_required(login_url='/login/')
def lovePoems_entry(request):
    title='Add Love Poem'
    form = NewLoveForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = ComputerForm(request.POST, request.FILES)
        if form.is_valid():
            lovePoems = form.save(commit=False)
            lovePoems.Admin = current_user
            lovePoems.admin_profile = profile
            lovePoems.save()

            messages.success(request,'Successfully saved')
        return redirect('lovePoems')

    else:
        
        form = NewLovePoem()

    return render(request,'poetry/lovePoems.html',{"form":form})

@login_required(login_url='/login/')
def angerPoems(request):
    
    angerPoems=Anger.objects.all()
    angerPoems=angerPoems[::-1]

    context={  
        'angerPoems':angerPoems, 
    }
    return render(request,'poetry/angerPoems.html', context)


@login_required(login_url='/login/')
def christianPoems(request):
    
    christianPoems=Christian.objects.all()
    christianPoems=christianPoems[::-1]

    context={  
        'christianPoems':christianPoems, 
    }
    return render(request,'poetry/christianPoems.html', context)




@login_required(login_url='/login/')
def coronavirusPoems(request):
    
    coronavirusPoems=Coronavirus.objects.all()
    coronavirusPoems=coronavirusPoems[::-1]

    context={  
        'coronavirusPoems':coronavirusPoems, 
    }
    return render(request,'poetry/coronavirus.html', context)


@login_required(login_url='/login/')
def deathPoems(request):
    
    deathPoems=Death.objects.all()
    deathPoems=deathPoems[::-1]

    context={  
        'deathPoems':deathPoems, 
    }
    return render(request,'poetry/deathPoems.html', context)

@login_required(login_url='/login/')
def familyPoems(request):
    
    familyPoems=Family.objects.all()
    familyPoems=familyPoems[::-1]

    context={  
        'familyPoems':familyPoems, 
    }
    return render(request,'poetry/familyPoems.html', context)


@login_required(login_url='/login/')
def friendshipPoems(request):
    
    friendshipPoems=Friendship.objects.all()
    friendshipPoems=friendshipPoems[::-1]

    context={  
        'friendshipPoems':friendshipPoems, 
    }
    return render(request,'poetry/friendshipPoems.html', context)


@login_required(login_url='/login/')
def holidayPoems(request):
    
    holidayPoems=Holiday.objects.all()
    holidayPoems=holidayPoems[::-1]

    context={  
        'holidayPoems':holidayPoems, 
    }
    return render(request,'poetry/holidayPoems.html', context)


@login_required(login_url='/login/')
def lifePoems(request):
    
    lifePoems=Life.objects.all()
    lifePoems=lifePoems[::-1]

    context={  
        'lifePoems':lifePoems, 
    }
    return render(request,'poetry/lifePoems.html', context)


@login_required(login_url='/login/')
def sadPoems(request):
    
    sadPoems=Sad.objects.all()
    sadPoems=sadPoems[::-1]

    context={  
        'sadPoems':sadPoems, 
    }
    return render(request,'poetry/sadPoems.html', context)


@login_required(login_url='/login/')
def spiritualPoems(request):
    
    spiritualPoems=Spiritual.objects.all()
    spiritualPoems=spiritualPoems[::-1]

    context={  
        'spiritualPoems':spiritualPoems, 
    }
    return render(request,'poetry/spiritual.html', context)


@login_required(login_url='/login/')
def naturePoems(request):
    
    naturePoems=Nature.objects.all()
    naturePoems=naturePoems[::-1]

    context={  
        'naturePoems':naturePoems, 
    }
    return render(request,'poetry/naturePoems.html', context)


