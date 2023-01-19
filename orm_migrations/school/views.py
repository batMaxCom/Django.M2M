from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    object_list = Student.objects.order_by('group').prefetch_related('teachers') # до prefetch_related было 6 запросов, после 4 (2 из которых системные, как я понял)
    context = {'object_list': object_list}
    return render(request, template, context)
