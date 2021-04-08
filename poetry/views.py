from django.shortcuts import render

from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from poetry.models import Love,Spiritual,Anger,Death,Family,Famous,Friendship,Holiday,Life,Nature,Sad,Christian,Coronavirus
from poetry.forms import NewAngerForm,NewChristianForm,NewCoronavirusForm,NewDeathForm,NewFamilyForm,NewFamousForm,NewFriendshipForm,NewHolidayForm,NewLifeForm,NewLoveForm,NewNatureForm,NewSadForm,NewSpiritualForm
from django.contrib import messages

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
        
        form = NewLoveForm(request.POST, request.FILES)
        if form.is_valid():
            lovePoems = form.save(commit=False)
            lovePoems.Admin = current_user
            lovePoems.admin_profile = profile
            lovePoems.save()

            messages.success(request,'Your poem has successifully being uploaded')
        return redirect('lovePoems')

    else:
        
        form = NewLoveForm()


    return render(request,'poetry/lovePoems_entry.html',{"form":form})

@login_required(login_url='/login/')
def angerPoems(request):
    
    angerPoems=Anger.objects.all()
    angerPoems=angerPoems[::-1]

    context={  
        'angerPoems':angerPoems, 
    }
    return render(request,'poetry/angerPoems_entry.html', context)


@login_required(login_url='/login/')
def angerPoems_entry(request):
    title='Add Anger Poem'
    form = NewAngerForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = NewAngerForm(request.POST, request.FILES)
        if form.is_valid():
            angerPoems = form.save(commit=False)
            angerPoems.Admin = current_user
            angerPoems.admin_profile = profile
            angerPoems.save()

            messages.success(request,'Successfully saved')
        return redirect('angerPoems')

    else:
        
        form = NewAngerForm()

    return render(request,'poetry/angerPoems_entry.html',{"form":form})


@login_required(login_url='/login/')
def christianPoems(request):
    
    christianPoems=Christian.objects.all()
    christianPoems=christianPoems[::-1]

    context={  
        'christianPoems':christianPoems, 
    }
    return render(request,'poetry/christianPoems.html', context)


@login_required(login_url='/login/')
def christianPoems_entry(request):
    title='Add Christian Poem'
    form = NewChristianForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = NewChristianForm(request.POST, request.FILES)
        if form.is_valid():
            christianPoems = form.save(commit=False)
            christianPoems.Admin = current_user
            christianPoems.admin_profile = profile
            christianPoems.save()

            messages.success(request,'Your poem has successifully being uploaded')
        return redirect('christianPoems')

    else:
        
        form = NewChristianForm()

    return render(request,'poetry/christianPoems_entry.html',{"form":form})


@login_required(login_url='/login/')
def coronavirusPoems(request):
    
    coronavirusPoems=Coronavirus.objects.all()
    coronavirusPoems=coronavirusPoems[::-1]

    context={  
        'coronavirusPoems':coronavirusPoems, 
    }
    return render(request,'poetry/coronavirus.html', context)

@login_required(login_url='/login/')
def coronavirusPoems_entry(request):
    title='Add Coronavirus Poem'
    form = NewCoronavirusForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = NewCoronavirusForm(request.POST, request.FILES)
        if form.is_valid():
            coronavirusPoems = form.save(commit=False)
            coronavirusPoems.Admin = current_user
            coronavirusPoems.admin_profile = profile
            coronavirusPoems.save()

            messages.success(request,'Your poem has successifully being uploaded')
        return redirect('coronavirusPoems')

    else:
        
        form = NewCoronavirusForm()

    return render(request,'poetry/coronavirusPoems_entry.html',{"form":form})


@login_required(login_url='/login/')
def deathPoems(request):
    
    deathPoems=Death.objects.all()
    deathPoems=deathPoems[::-1]

    context={  
        'deathPoems':deathPoems, 
    }
    return render(request,'poetry/deathPoems.html', context)


@login_required(login_url='/login/')
def deathPoems_entry(request):
    title='Add Death Poem'
    form = NewDeathForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = NewDeathForm(request.POST, request.FILES)
        if form.is_valid():
            deathPoems = form.save(commit=False)
            deathPoems.Admin = current_user
            deathPoems.admin_profile = profile
            deathPoems.save()

            messages.success(request,'Your poem has successifully being uploaded')
        return redirect('deathPoems')

    else:
        
        form = NewDeathForm()

    return render(request,'poetry/deathPoems_entry.html',{"form":form})



@login_required(login_url='/login/')
def familyPoems(request):
    
    familyPoems=Family.objects.all()
    familyPoems=familyPoems[::-1]

    context={  
        'familyPoems':familyPoems, 
    }
    return render(request,'poetry/familyPoems.html', context)


@login_required(login_url='/login/')
def familyPoems_entry(request):
    title='Add Family Poem'
    form = NewFamilyForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = NewFamilyForm(request.POST, request.FILES)
        if form.is_valid():
            familyPoems = form.save(commit=False)
            familyPoems.Admin = current_user
            familyPoems.admin_profile = profile
            familyPoems.save()

            messages.success(request,'Your poem has successifully being uploaded')
        return redirect('familyPoems')

    else:
        
        form = NewFamilyForm()

    return render(request,'poetry/familyPoems_entry.html',{"form":form})


@login_required(login_url='/login/')
def friendshipPoems(request):
    
    friendshipPoems=Friendship.objects.all()
    friendshipPoems=friendshipPoems[::-1]

    context={  
        'friendshipPoems':friendshipPoems, 
    }
    return render(request,'poetry/friendshipPoems.html', context)


@login_required(login_url='/login/')
def friendshipPoems_entry(request):
    title='Add Friendship Poem'
    form = NewFriendshipForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = NewFriendshipForm(request.POST, request.FILES)
        if form.is_valid():
            friendshipPoems = form.save(commit=False)
            friendshipPoems.Admin = current_user
            friendshipPoems.admin_profile = profile
            friendshipPoems.save()

            messages.success(request,'Your poem has successifully being uploaded')
        return redirect('friendshipPoems')

    else:
        
        form = NewFriendshipForm()

    return render(request,'poetry/friendshipPoems_entry.html',{"form":form})



@login_required(login_url='/login/')
def holidayPoems(request):
    
    holidayPoems=Holiday.objects.all()
    holidayPoems=holidayPoems[::-1]

    context={  
        'holidayPoems':holidayPoems, 
    }
    return render(request,'poetry/holidayPoems.html', context)



@login_required(login_url='/login/')
def holidayPoems_entry(request):
    title='Add Holiday Poem'
    form = NewHolidayForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = NewHolidayForm(request.POST, request.FILES)
        if form.is_valid():
            holidayPoems = form.save(commit=False)
            holidayPoems.Admin = current_user
            holidayPoems.admin_profile = profile
            holidayPoems.save()

            messages.success(request,'Your poem has successifully being uploaded')
        return redirect('holidayPoems')

    else:
        
        form = NewHolidayForm()

    return render(request,'poetry/holidayPoems_entry.html',{"form":form})


@login_required(login_url='/login/')
def lifePoems(request):
    
    lifePoems=Life.objects.all()
    lifePoems=lifePoems[::-1]

    context={  
        'lifePoems':lifePoems, 
    }
    return render(request,'poetry/lifePoems.html', context)

@login_required(login_url='/login/')
def lifePoems_entry(request):
    title='Add Life Poem'
    form = NewLifeForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = NewLifeForm(request.POST, request.FILES)
        if form.is_valid():
            lifePoems = form.save(commit=False)
            lifePoems.Admin = current_user
            lifePoems.admin_profile = profile
            lifePoems.save()

            messages.success(request,'Your poem has successifully being uploaded')
        return redirect('lifePoems')

    else:
        
        form = NewLifeForm()

    return render(request,'poetry/lifePoems_entry.html',{"form":form})


@login_required(login_url='/login/')
def sadPoems(request):
    
    sadPoems=Sad.objects.all()
    sadPoems=sadPoems[::-1]

    context={  
        'sadPoems':sadPoems, 
    }
    return render(request,'poetry/sadPoems.html', context)

@login_required(login_url='/login/')
def sadPoems_entry(request):
    title='Add Sad Poem'
    form = NewSadForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = NewSadForm(request.POST, request.FILES)
        if form.is_valid():
            sadPoems = form.save(commit=False)
            sadPoems.Admin = current_user
            sadPoems.admin_profile = profile
            sadPoems.save()

            messages.success(request,'Your poem has successifully being uploaded')
        return redirect('sadPoems')

    else:
        
        form = NewSadForm()

    return render(request,'poetry/sadPoems_entry.html',{"form":form})


@login_required(login_url='/login/')
def spiritualPoems(request):
    
    spiritualPoems=Spiritual.objects.all()
    spiritualPoems=spiritualPoems[::-1]

    context={  
        'spiritualPoems':spiritualPoems, 
    }
    return render(request,'poetry/spiritual.html', context)

@login_required(login_url='/login/')
def spiritualPoems_entry(request):
    title='Add Spiritual Poem'
    form = NewSpiritualForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = NewSpiritualForm(request.POST, request.FILES)
        if form.is_valid():
            spiritualPoems = form.save(commit=False)
            spiritualPoems.Admin = current_user
            spiritualPoems.admin_profile = profile
            spiritualPoems.save()

            messages.success(request,'Your poem has successifully being uploaded')
        return redirect('spiritualPoems')

    else:
        
        form = NewSpiritualForm()

    return render(request,'poetry/spiritualPoems_entry.html',{"form":form})


@login_required(login_url='/login/')
def naturePoems(request):
    
    naturePoems=Nature.objects.all()
    naturePoems=naturePoems[::-1]

    context={  
        'naturePoems':naturePoems, 
    }
    return render(request,'poetry/naturePoems.html', context)


@login_required(login_url='/login/')
def naturePoems_entry(request):
    title='Add Nature Poem'
    form = NewNatureForm(request.POST or None)
    current_user = request.user
    profile = request.user.profile

    if request.method == 'POST':
        
        form = NewNatureForm(request.POST, request.FILES)
        if form.is_valid():
            naturePoems = form.save(commit=False)
            naturePoems.Admin = current_user
            naturePoems.admin_profile = profile
            naturePoems.save()

            messages.success(request,'Your poem has successifully being uploaded')
        return redirect('naturePoems')

    else:
        
        form = NewNatureForm()

    return render(request,'poetry/naturePoems_entry.html',{"form":form})