from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
import sweetify

# from rest_framework import generics, permissions, mixins
# from rest_framework.response import Response
# from .serializer import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from sweetify.views import SweetifySuccessMixin

# Create your views here.
# class TestUpdateView(SweetifySuccessMixin, UpdateView):
#     model = TestModel
#     fields = ['text']
#     success_message = 'TestModel successfully updated!'


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
            
            messages.success(request, f'Account has been created.You can now log in.')

            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', { 'form':form })


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')

            messages.success(request, f'Account has been updated')


            return redirect('display_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


def display_profile(request):

    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    

    context = {
        'u_form': u_form,
        'p_form': p_form,
       
    }
    return render(request, 'users/display_profile.html', context)


# class RegisterApi(generics.GenericAPIView):
#     serializer_class = RegisterSerializer
#     def post(self, request, *args,  **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": UserSerializer(user,    context=self.get_serializer_context()).data,
#             "message": "User Created Successfully.  Now perform Login to get your token",
#         })
