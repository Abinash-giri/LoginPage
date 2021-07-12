from django.shortcuts import render

from django.http import HttpResponse

from .models import Course

def index(request):
    # return HttpResponse('Hello there!')
    courses = Course.objects

    return render(request, 'courses/index.html', {'courses':courses})
