from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Subject, Student, Teacher
# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = 'blog/index.html'


# def navigation(request):
#     from django.http import HttpResponse
#     from django.template import loader
#
#     template = loader.get_template('blog/navigation_bar.html')
#     return HttpResponse(template.render())
#

class SubjectListView(ListView):
    template_name = 'blog/subjects.html'
    model = Subject
    context_object_name = 'subjects'


class StudentListView(ListView):
    template_name = 'blog/students.html'
    model = Student
    context_object_name = 'students'


class TeacherListView(ListView):
    template_name = 'blog/teachers.html'
    model = Teacher
    context_object_name = 'teachers'



# class ProductListView(LoginRequiredMixin, ListView):
#     login_url = '/signin/'
#     template_name = 'main/products.html'
#     model = Product
#     context_object_name = 'products'
