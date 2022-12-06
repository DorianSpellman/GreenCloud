from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from eco import views
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, Ваш аккаунт успешно создан.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'title' : 'Авторизация',
        'menu' : views.menu,
        'form' : form
    }
    
    return render(request, 'users/register.html', context=context)

@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title' : 'Профиль',
        'menu' : views.menu,
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context=context)