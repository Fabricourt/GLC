from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team', 'phone', 'email', 'timestamp')
admin.site.register(Team, TeamAdmin)