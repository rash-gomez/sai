from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.views import generic

# from drug.models import Drugs
from core.models import Profile
from sai.settings import AUTH_USER_MODEL
from core.permissions.mixins import AdminPermissionRequiredMixin, StaffPermissionRequiredMixin


User = AUTH_USER_MODEL


# class DrugSearchListView(LoginRequiredMixin, generic.ListView):
#     template_name = 'search/view.html'
#     paginate_by = 5
#     context_object_name = 'drugs'
#
#     def get_context_data(self, **kwargs):
#         context = super(DrugSearchListView, self).get_context_data(**kwargs)
#         context['query'] = self.request.GET.get('q')
#         context['pharmacy'] = Pharmacy.objects.filter(
#             name=self.request.user.pharmacyuser.works_at)[0]
#         context['pharmacy_drugs'] = Drugs.objects.filter(
#             pharmacy=self.request.user.pharmacyuser.works_at)
#         return context
#
#     def get_queryset(self):
#         request = self.request
#         query = request.GET.get('q')
#
#         if query is not None:
#             return Drugs.objects.search(query)
#         return Drugs.objects.none()


class StaffSearchListView(LoginRequiredMixin, generic.ListView):
    template_name = 'search/staff_list.html'
    paginate_by = 5
    context_object_name = 'profiles'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super(StaffSearchListView, self).get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            lookups = Q(user__email__icontains=query) | Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query)
            return Profile.objects.filter(lookups, user__is_admin=False, user__is_superuser=False).distinct()
            # return User.objects.search(query)
        return User.objects.none()
