from django.shortcuts import render, HttpResponse
from .models import ToMeet, Goal_for_month


def homework(request):
    return render(request, 'homework.html')


def hw_2(request):
    return HttpResponse('Добро пожаловать в приложение ToDo - Admin) ')


def show_meetings(request):
    all_meetings = ToMeet.objects.all()
    variables = {
        'meetings': all_meetings
    }
    return render(request, 'meeting.html', context=variables)


def show_goals_for_month(request):
    goals = Goal_for_month.objects.all()
    return render(request, 'goals.html', {'goals': goals})