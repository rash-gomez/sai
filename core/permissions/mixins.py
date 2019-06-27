from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


class AdminPermissionRequiredMixin:
    # This mixin will redirect the users back to apply list is user is not an admin

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin:
            messages.info(request, "You do not have required permissions")
            return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)


class StaffPermissionRequiredMixin:
    # This mixin will redirect the users back to apply list is user is not an pharmacist

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_school_staff:
            messages.info(request, "You do not have required permissions")
            return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)


class StudentPermissionRequiredMixin:
    # This mixin will redirect the users back to apply list is user is not an pharmacist

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_student:
            messages.info(request, "You do not have required permissions")
            return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)


# function based permission decorators
def admin_required_permission(function):

    def admin_permission(request, *args, **kwargs):

        if not request.user.is_admin:
            messages.info(request, "You do not have required permissions")
            return redirect('home')
        else:
            return function(request, *args, **kwargs)

    return admin_permission


def staff_required_permission(function):

    def staff_permission(request, *args, **kwargs):

        if not request.user.is_school_staff:
            messages.info(request, "You do not have required permissions")
            return redirect('home')
        else:
            return function(request, *args, **kwargs)

    return staff_permission


def student_required_permission(function):

    def student_permission(request, *args, **kwargs):

        if not request.user.is_student:
            messages.info(request, "You do not have required permissions")
            return redirect('home')
        else:
            return function(request, *args, **kwargs)

    return student_permission
