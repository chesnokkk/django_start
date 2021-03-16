from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm
from .models import Mess
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.mail import send_mail

def sending(request):
    return render(request,'users/sending.html')

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} учспкшно создан')
            return redirect('/')

    else:
        form = UserRegisterForm()

    return render(request,'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == "POST":
        profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if profileForm.is_valid() and updateUserForm.is_valid():
            updateUserForm.save()
            profileForm.save()
            messages.success(request, f'Ваш аккаунт обновлен!')
            return redirect('profile')
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)



    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm
    }
    return render(request, 'users/profile.html', data)

class MessCreateView(CreateView):
    template_name = 'users/mess.html'
    model = Mess

    subject = "Тема сообщения"
    plain_message = "Текст сообщения"
    from_email = "testpost1122@gmail.com"
    to = "nahervihuher1@gmail.com"
    send_mail(subject, plain_message, from_email, [to])

    fields = ['title', 'email', 'message']
