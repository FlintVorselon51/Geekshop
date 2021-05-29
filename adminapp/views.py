from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from authapp.models import User
from mainapp.models import ProductCategory
from adminapp.forms import UserAdminForm, CategoryAdminForm


def check_user(user):
    return user.is_superuser or user.is_staff


@user_passes_test(check_user)
def index(request):
    return render(request, 'adminapp/admin.html')


class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(check_user))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminForm
    success_url = reverse_lazy('adminapp:users_read')

    @method_decorator(user_passes_test(check_user))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminForm
    success_url = reverse_lazy('adminapp:users_read')

    @method_decorator(user_passes_test(check_user))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('adminapp:users_read')

    @method_decorator(user_passes_test(check_user))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/admin-categories-read.html'

    @method_decorator(user_passes_test(check_user))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryListView, self).dispatch(request, *args, **kwargs)


class CategoryCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-categories-create.html'
    form_class = CategoryAdminForm
    success_url = reverse_lazy('adminapp:categories_read')

    @method_decorator(user_passes_test(check_user))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, *args, **kwargs)


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/admin-categories-update-delete.html'
    form_class = UserAdminForm
    success_url = reverse_lazy('adminapp:categories_read')

    @method_decorator(user_passes_test(check_user))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)


class CategoryDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('adminapp:categories_read')

    @method_decorator(user_passes_test(check_user))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request, *args, **kwargs)

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
