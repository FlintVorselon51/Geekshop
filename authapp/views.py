from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView

from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from basketapp.models import Basket
from authapp.models import User


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'title': 'Geekshop - Авторизация', 'form': form}
    return render(request, 'authapp/login.html', context=context)


class CreateUserView(CreateView):
    model = User
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            pass
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Geekshop - профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user)
    }
    return render(request, 'authapp/profile.html', context)
