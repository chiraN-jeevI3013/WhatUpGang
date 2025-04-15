from django.contrib import admin
from .models import Team, Member, Event

admin.site.register(Team)
admin.site.register(Member)
admin.site.register(Event)