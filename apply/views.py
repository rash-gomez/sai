from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from apply import forms
from core.models import User
from apply.models import Student, Document

# print links
from apply.utils import render_to_pdf
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa

from core.permissions.mixins import (AdminPermissionRequiredMixin,
                                     StaffPermissionRequiredMixin,
                                     StudentPermissionRequiredMixin,
                                     admin_required_permission,
                                     staff_required_permission,
                                     student_required_permission)

# Create your views here.


class StudentNewApplication(LoginRequiredMixin, generic.CreateView):
    template_name = 'apply/register.html'
    form_class = forms.DocumentsForm

    def form_valid(self, form):
        form.instance.student = self.request.user
        form.instance.nationality = self.request.user.nationality
        form.instance.entry_date = timezone.now()

        # check if user already registered for this session
        student_now = self.request.user
        docs = Document.objects.all()
        month = timezone.now().strftime('%B')

        for doc in docs:
            doc_month = doc.entry_date.strftime('%B')
            doc_student = doc.student

            if doc_month == month and student_now == doc_student:
                messages.error(
                    self.request, 'Already registered for this session')
                return redirect('home')
            else:
                pass

        form.save()

        return super().form_valid(form)

    def get_success_url(self):
        # pharmacy = self.kwargs.get('pharmacy')
        return reverse('home')


class StudentOldApplication(LoginRequiredMixin, generic.ListView):
    template_name = 'apply/old_applications.html'
    model = Document
    context_object_name = 'docs'

    def get_queryset(self):
        docs = Document.objects.filter(student=self.request.user)
        return docs


class ApplicationList(LoginRequiredMixin, generic.ListView):
    template_name = 'apply/list_applications.html'
    model = Document
    context_object_name = 'docs'
    queryset = Document.objects.all()


class ApplicationDetails(LoginRequiredMixin, generic.DetailView):
    template_name = 'apply/detail_applications.html'
    model = Document
    context_object_name = 'doc'
    queryset = Document.objects.all()

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        doc = get_object_or_404(Document, pk=pk)

        return doc


class ApplicationEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = 'apply/edit_application.html'
    model = Document
    form_class = forms.DocumentsForm

    def get_success_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        return reverse('apply:detail_application', kwargs={'pk': pk})

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        doc = get_object_or_404(Document, pk=pk)

        return doc


class ApplicationDelete(LoginRequiredMixin, generic.DeleteView):
    template_name = 'apply/delete_application.html'
    model = Document
    context_object_name = 'doc'
    success_url = reverse_lazy('apply:list_application')


# printing list of applicants
# def render_pdf_view(request):
#     template_path = 'apply/applicants.html'
#
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#
#     # find the template and render it.
#     template = get_template(template_path)
#     context = Context({'pagesize': 'A4'})
#     html = template.render(Context(context))
#
#     # create a pdf
#     pisaStatus = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
#
#     # if error then show some funy view
#
#     if pisaStatus.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#
#     return response


# Creating our view, it is a class based view
class GeneratePdf(generic.View):
    def get(self, request, *args, **kwargs):
        # getting the template
        pdf = render_to_pdf('apply/applicants.html')

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


# @login_required()
# def student_application(request):
#     if request.method == 'POST':
#         # student_form = forms.StudentRegisterForm(request.POST, request.FILES, instance=request.user)
#         files_form = forms.DocumentsForm(
#             request.POST, request.FILES)
#
#         if files_form.is_valid():
#             # student_form.instance.student = request.user
#             # student_form.save()
#             files_form.save()
#             messages.success(request, 'application submit was successful')
#             return redirect('home')
#
#     else:
#         # student_form = forms.StudentRegisterForm(instance=request.user)
#         files_form = forms.DocumentsForm()
#
#     context = {
#         # 'form1': student_form,
#         'form2': files_form,
#     }
#
#     return render(request, 'apply/register.html', context)
