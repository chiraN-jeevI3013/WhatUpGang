from django.shortcuts import render
from .models import Team, Event

def home(request):
    teams = Team.objects.all()
    events = Event.objects.all()
    return render(request, 'home.html', {'teams': teams, 'events': events})