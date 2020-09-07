from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from django.core.mail import send_mail
from django.conf import settings
from .models import Student

class HomeView(ListView):
    model = Student
    # by default template is modelname_list.html
    template_name = 'student_app/home.html'
    # by default context object name is (modelname_list)
    context_object_name = 'my_students'


class StudentDetailView(DetailView):
    model = Student
    # by default template_name is student_detail.html
    # by default context is student_object (or) student
    # generic detail view should use pk or slug only fileds in url.


class CreateStudentView(CreateView):
    model = Student
    fields = ('name','email','address','income')
    # we can either use success_url or implement get_absolute_url in model.
    success_url = reverse_lazy('student_app:home')   # /home/
    # default template is student_form.html  [we need to create this.]
    # conext object name is student


class UpdateStudentView(UpdateView):
    model = Student
    fields = ('name', 'email')
    success_url = reverse_lazy('student_app:home')
    template_name = 'student_app/student_form_update.html'


class DeleteStudentView(DeleteView):
    model = Student
    # delete view requires the template as 'student_confirm_delete.html'
    # either we can create one or we can choose other by template_name param.
    # must required success_url after deleteion success..
    success_url = reverse_lazy('student_app:home')

def sendEmail(request):
    if request.method == "POST":
        to = request.POST.get('to')
        content = request.POST.get('content')
        send_mail(
            'High Priority Email Check Now!!',
            content,
            settings.EMAIL_HOST_USER,
            [to],
            fail_silently=False,
        )
        return redirect('student_app:home')
    return render(request, 'student_app/send_email.html', {})
