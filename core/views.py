from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from core import forms
from core.models import User
from core.permissions.mixins import (AdminPermissionRequiredMixin,
                                     StaffPermissionRequiredMixin,
                                     StudentPermissionRequiredMixin,
                                     admin_required_permission,
                                     staff_required_permission,
                                     student_required_permission)

# Create your views here.


class LandingView(generic.TemplateView):
    template_name = "core/landing.html"
    # model = User
    # paginate_by = 5
    # context_object_name = 'users'
    # queryset = User.objects.all()


class IndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "core/index.html"
    model = User
    paginate_by = 5
    context_object_name = 'users'
    queryset = User.objects.all()


class UserProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = 'core/profile.html'
    model = User
    queryset = User.objects.all()


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = forms.UserProfile(request.POST, instance=request.user)
        p_form = forms.ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile was successfully updated')
            return redirect('core:profile', name=request.user.first_name)

    else:
        u_form = forms.UserProfile(instance=request.user)
        p_form = forms.ProfileForm(instance=request.user.profile)

    context = {
        'form1': u_form,
        'form2': p_form,
    }

    return render(request, 'core/profile_update.html', context)


class UserList(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'core/staff_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_admin=False, is_superuser=False)


@login_required(login_url=reversed('account_login'))
@admin_required_permission
def staff_add(request):
    if request.method == 'POST':
        # print(request.POST)
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)

        if user.is_school_staff:
            user.is_school_staff = False
            messages.success(
                request, f'{user.email} was successfully removed as a Staff')
        else:
            user.is_school_staff = True
            messages.success(
                request, f'{user.email} was successfully added as a staff')
        user.save()
        return redirect('core:user_list')
    else:
        return Http404("Forbidden request type")

