from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from.models import Team

def index(request):
  teams = Team.objects.order_by('-timestamp').filter(is_published=True)

  paginator = Paginator(teams, 6)
  page = request.GET.get('page')
  paged_teams = paginator.get_page(page)

  context = {
    'teams': paged_teams
  }

  return render(request, 'teams/teams.html', context)

def team(request, team_id):
  team = get_object_or_404(team, pk=team_id)

  context = {
    'team': team
  }

  return render(request, 'teams/team.html', context)
