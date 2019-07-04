from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from about.models import About, header, category, numbers
from home.models import Topbar, Head, Footer
from graduates.models import Graduate
from team.models import Team
from gallerys.models import Photo
from events.models import Event
from accounts.models import Profile
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import (
    ListView,
)

# Dont Repeat Yourself = DRY

def index(request):
    abouts = About.objects.order_by('-reload').filter(is_published=True)[:1]
    graduates = Graduate.objects.order_by('-timestamp').filter(is_published=True)[:1]
    numberss = numbers.objects.order_by('reload').filter(is_published=True)[:4]
    teams = Team.objects.order_by('-timestamp').filter(is_published=True)[:4]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    heads = Head.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    categorys = category.objects.order_by('-reload').filter(is_published=True)[:4]
    photos = Photo.objects.order_by('-reload').filter(is_published=True)[:6]
    accounts = Profile.objects.all()

    context = {
        'events': Event.objects.all()[:3],
        'abouts': abouts,
        'graduates': graduates,
        'numberss': numberss,
        'accounts': accounts,
        'topbars': topbars,
        'heads': heads,
        'footers': footers,
        'teams': teams,
        'categorys': categorys,
        'photos': photos,
    }
    return render(request, 'pages/index.html', context) 


class EventListView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'
    ordering = ['-created_on']
    paginate_by = 5

def about(request):
    teams = Team.objects.order_by('-timestamp').filter(is_published=True)[:4]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    abouts = About.objects.order_by('-reload').filter(is_published=True)[:1]
    headers = header.objects.order_by('-reload').filter(is_published=True)[:1]
    categorys = category.objects.order_by('reload').filter(is_published=True)
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    
    context = {
        'topbars': topbars,
        'teams': teams,
        'headers': headers,
        'categorys': categorys,
        'abouts': abouts,
        'footers': footers
    }
    return render(request, 'pages/about.html', context) 

@staff_member_required
def mobile(request):
    return render(request, 'pages/mobile.html') 

@staff_member_required
def tablet(request):
    return render(request, 'pages/tablet.html') 

@staff_member_required
def laptop(request):
    return render(request, 'pages/laptop.html') 