from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from teachers.models import Teacher
from courses.models import Course


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'
    # queryset = Teacher.objects.all()[:1]
# Create your views here.


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher.html'
    context_object_name = 'teacher'


def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)
    # Add in a QuerySet of all the books
    context['courses'] = Course.objects.filter(
        available=True,  teacher=self.kwargs['pk'])
    return context
