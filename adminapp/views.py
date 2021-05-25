from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from mainapp.models import ProductCategory
from adminapp.forms import UserAdminForm, CategoryAdminForm


def check_user(user):
    return user.is_superuser or user.is_staff


@user_passes_test(check_user)
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(check_user)
def users_read(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(check_user)
def users_create(request):
    if request.method == 'POST':
        form = UserAdminForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('admin_staff:users_read'))
    else:
        form = UserAdminForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(check_user)
def users_update(request, user_id):
    selected_user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminForm(data=request.POST, files=request.FILES, instance=selected_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('admin_staff:users_read'))
        else:
            print(form.errors)
    else:
        form = UserAdminForm(instance=selected_user)
    context = {'form': form, 'selected_user': selected_user}
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(check_user)
def users_remove(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse_lazy('admin_staff:users_read'))


@user_passes_test(check_user)
def categories_read(request):
    context = {'categories': ProductCategory.objects.all()}
    return render(request, 'adminapp/admin-categories-read.html', context)


@user_passes_test(check_user)
def categories_create(request):
    if request.method == 'POST':
        form = CategoryAdminForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('admin_staff:categories_read'))
    else:
        form = CategoryAdminForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-categories-create.html', context)


@user_passes_test(check_user)
def categories_update(request, category_id):
    selected_category = ProductCategory.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoryAdminForm(data=request.POST, instance=selected_category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('admin_staff:categories_read'))
    else:
        form = CategoryAdminForm(instance=selected_category)
    context = {'form': form, 'selected_category': selected_category}
    return render(request, 'adminapp/admin-categories-update-delete.html', context)


@user_passes_test(check_user)
def categories_remove(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    category.delete()
    return HttpResponseRedirect(reverse_lazy('admin_staff:categories_read'))
